---
declaration: def
origin: cited
lean: TauCeti.Schreier.stabilizerEquiv
statement: formalized
---

# Reidemeister--Schreier presentation theorem

Rewriting the defining relations at
every state and killing representative-word rewrites presents the actual point stabilizer,
provided inverse representatives reach every state and the base representative evaluates to one.
All generators, including redundant edges, retain their specified word dictionary.

```lean
TauCeti.Schreier.stabilizerEquiv.{u_1, u_2} {α : Type u_1} {Q : Type u_2}
  (W : Set (TauCeti.PresentationWord α)) [action : MulAction (PresentedGroup (FreeGroup.mk '' W)) Q]
  (b : Q) (r : Q → TauCeti.PresentationWord α)
  (hr : ∀ (q : Q), ((PresentedGroup.mk (FreeGroup.mk '' W)) (FreeGroup.mk (r q)))⁻¹ • b = q)
  (hb : (PresentedGroup.mk (FreeGroup.mk '' W)) (FreeGroup.mk (r b)) = 1) :
  PresentedGroup
      (TauCeti.Schreier.stabilizerRelators (TauCeti.Schreier.actionPerm PresentedGroup.of) W b r) ≃*
    ↥(MulAction.stabilizer (PresentedGroup (FreeGroup.mk '' W)) b)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Schreier.stabilizerEquiv`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Presentation/Schreier/Presentation.html#TauCeti.Schreier.stabilizerEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.Schreier.stabilizerEquiv`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Presentation/Schreier/Presentation.html#TauCeti.Schreier.stabilizerEquiv)
- [Source of `TauCeti.Schreier.stabilizerEquiv` in TauCeti/GroupTheory/Presentation/Schreier/Presentation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/Presentation/Schreier/Presentation.lean#L188)
