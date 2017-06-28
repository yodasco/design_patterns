# Design pattern toolkit.

A small set of design pattern I miss as idioms in `python`.

# Examples:

1. Scope Guard. A [simple pattern](https://en.wikibooks.org/wiki/More_C%2B%2B_Idioms/Scope_Guard)
   for operations one needs when exiting a scope.
   Example:
   ```python
   with ScopeGuard(my_cleanup_function):
        # Some code...
   ```

