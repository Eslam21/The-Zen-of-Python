import warnings
from .new_module import new_function
from .old_module import old_function

# # Issue a deprecation warning for old_function
def old_function():
    warnings.warn(
        "old_function is deprecated and will be removed in a future release. "
        "Use new_function instead.",
        DeprecationWarning,
        stacklevel=2
    )
    # Call the old implementation (optional)
    print("This is the old function (deprecated).")

__all__ = ['new_function']
