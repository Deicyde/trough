---
catalog: module
lean: Cslib.LTS.toFrame, Cslib.LTS.toFrame_r_iff_tr, Cslib.LTS.toFrame_diagonal_iff_tr
statement: formalized
proof: formalized
---

# Modal Frames and LTS

`Cslib.Foundations.Semantics.Frame.LTS`, in [Cslib/Foundations/Semantics/Frame/LTS.lean](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/Semantics/Frame/LTS.lean), by Fabrizio Montesi.

`Cslib.LTS.toFrame` (definition, [line 24](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/Semantics/Frame/LTS.lean#L24))

> Transforms `lts` into a corresponding unary `Frame`.

```lean
def toFrame : Frame State (mkUnary Label)
```

`Cslib.LTS.toFrame_r_iff_tr` (lemma, [line 29](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/Semantics/Frame/LTS.lean#L29))

```lean
lemma toFrame_r_iff_tr : lts.toFrame.r μ s f ↔ lts.Tr s μ (f default)
```

`Cslib.LTS.toFrame_diagonal_iff_tr` (lemma, [line 32](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/Semantics/Frame/LTS.lean#L32))

```lean
lemma toFrame_diagonal_iff_tr : lts.toFrame.diagonal μ s s' ↔ lts.Tr s μ s'
```

## Depends on

- [Modal Frames](basic.md)
- [Labelled Transition System (LTS)](../lts/basic.md)

## Sources

- [Cslib/Foundations/Semantics/Frame/LTS.lean at 7c95c37f](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/Semantics/Frame/LTS.lean)
- [Declaration ledger](../../../../../sources/cslib/Cslib.Foundations.Semantics.Frame.LTS.json)
