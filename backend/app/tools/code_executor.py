"""
WeaR Ai - Code Executor Tool
Sandboxed Python code execution.
"""

import asyncio
import sys
import io
import traceback
from contextlib import redirect_stdout, redirect_stderr
from typing import Any

from app.tools.base import BaseTool, ToolOutput


class CodeExecutorTool(BaseTool):
    """Execute Python code in a sandboxed environment."""
    
    # Restricted imports for safety
    ALLOWED_MODULES = {
        "math", "statistics", "random", "datetime", "json", "re",
        "collections", "itertools", "functools", "operator",
        "string", "textwrap", "unicodedata",
        "decimal", "fractions",
        "copy", "pprint",
    }
    
    @property
    def name(self) -> str:
        return "code_executor"
    
    @property
    def description(self) -> str:
        return "Execute Python code to perform calculations, data processing, or solve problems. Returns stdout, stderr, and any returned value."
    
    @property
    def parameters_schema(self) -> dict:
        return {
            "type": "object",
            "properties": {
                "code": {
                    "type": "string",
                    "description": "Python code to execute",
                },
                "timeout": {
                    "type": "integer",
                    "description": "Execution timeout in seconds (default: 30, max: 60)",
                    "default": 30,
                },
            },
            "required": ["code"],
        }
    
    async def execute(self, code: str, timeout: int = 30, **kwargs) -> ToolOutput:
        """Execute Python code in a sandboxed environment."""
        timeout = min(timeout, 60)  # Cap at 60 seconds
        
        try:
            # Run in a thread pool to not block the event loop
            result = await asyncio.wait_for(
                asyncio.get_event_loop().run_in_executor(
                    None, self._execute_code, code
                ),
                timeout=timeout,
            )
            return result
        except asyncio.TimeoutError:
            return ToolOutput(
                success=False,
                result=f"Code execution timed out after {timeout} seconds",
                error="timeout",
            )
        except Exception as e:
            return ToolOutput(
                success=False,
                result=f"Execution error: {str(e)}",
                error=str(e),
            )
    
    def _execute_code(self, code: str) -> ToolOutput:
        """Execute code synchronously with restricted globals."""
        stdout_capture = io.StringIO()
        stderr_capture = io.StringIO()
        
        # Create restricted globals
        restricted_globals = {
            "__builtins__": self._get_safe_builtins(),
            "__name__": "__main__",
        }
        
        # Import allowed modules
        for module_name in self.ALLOWED_MODULES:
            try:
                restricted_globals[module_name] = __import__(module_name)
            except ImportError:
                pass
        
        result_value = None
        
        try:
            with redirect_stdout(stdout_capture), redirect_stderr(stderr_capture):
                # Compile and execute
                compiled = compile(code, "<sandbox>", "exec")
                exec(compiled, restricted_globals)
                
                # Check if there's a result variable
                if "result" in restricted_globals:
                    result_value = restricted_globals["result"]
            
            stdout_output = stdout_capture.getvalue()
            stderr_output = stderr_capture.getvalue()
            
            # Format output
            output_parts = []
            if stdout_output:
                output_parts.append(f"**Output:**\n```\n{stdout_output}\n```")
            if stderr_output:
                output_parts.append(f"**Stderr:**\n```\n{stderr_output}\n```")
            if result_value is not None:
                output_parts.append(f"**Result:** `{repr(result_value)}`")
            
            if not output_parts:
                output_parts.append("Code executed successfully with no output.")
            
            return ToolOutput(
                success=True,
                result="\n\n".join(output_parts),
                data={
                    "stdout": stdout_output,
                    "stderr": stderr_output,
                    "result": result_value,
                },
            )
            
        except Exception as e:
            error_trace = traceback.format_exc()
            return ToolOutput(
                success=False,
                result=f"**Error:**\n```\n{error_trace}\n```",
                error=str(e),
            )
    
    def _get_safe_builtins(self) -> dict:
        """Get a restricted set of builtins."""
        safe_builtins = {}
        
        # Safe functions
        allowed_builtins = [
            # Types
            "bool", "int", "float", "str", "list", "dict", "tuple", "set", "frozenset",
            "bytes", "bytearray", "complex", "type",
            # Functions
            "abs", "all", "any", "bin", "chr", "divmod", "enumerate", 
            "filter", "format", "hash", "hex", "id", "isinstance", "issubclass",
            "iter", "len", "map", "max", "min", "next", "oct", "ord", 
            "pow", "print", "range", "repr", "reversed", "round", "slice",
            "sorted", "sum", "zip",
            # Exceptions
            "Exception", "ValueError", "TypeError", "KeyError", "IndexError",
            "AttributeError", "RuntimeError", "StopIteration", "ZeroDivisionError",
            # Constants
            "True", "False", "None",
        ]
        
        for name in allowed_builtins:
            if hasattr(__builtins__, name):
                safe_builtins[name] = getattr(__builtins__, name)
            elif name in __builtins__:
                safe_builtins[name] = __builtins__[name]
        
        return safe_builtins
