---
catalog: module
lean: Cedar.Spec.Decision, Cedar.Spec.Response
statement: formalized
proof: formalized
---

# Response

`Cedar.Spec.Response`, in [Cedar/Spec/Response.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Response.lean).

> This file defines Cedar responses.

`Cedar.Spec.Decision` (inductive type, [line 31](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Response.lean#L31))

```lean
public inductive Decision where
  | allow
  | deny
```

`Cedar.Spec.Response` (structure, [line 35](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Response.lean#L35))

```lean
public structure Response where
  decision : Decision
  determiningPolicies : Set PolicyID
  erroringPolicies : Set PolicyID
```

## Depends on

- [Spec/Policy](policy.md)

## Sources

- [Cedar/Spec/Response.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Response.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Spec.Response.json)
