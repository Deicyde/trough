---
declaration: def
origin: cited
lean: TauCeti.endAlgEquivOfSimple
statement: formalized
---

# Schur's lemma as an identification of algebras

the endomorphisms of a simple object `X`
with finite-dimensional endomorphisms over an algebraically closed field `k` are the scalars
`k`. This is the inverse of the structure map `algebraMap k (End X)`, `c ↦ c • 𝟙 X`.

```lean
TauCeti.endAlgEquivOfSimple.{w, v, u} (k : Type w) [Field k] [IsAlgClosed k] {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Preadditive C] [CategoryTheory.Linear k C]
  [CategoryTheory.Limits.HasKernels C] (X : C) [CategoryTheory.Simple X]
  [FiniteDimensional k (X ⟶ X)] : CategoryTheory.End X ≃ₐ[k] k
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.endAlgEquivOfSimple`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Preadditive/Schur.html#TauCeti.endAlgEquivOfSimple).

## Sources

- [Tau Ceti documentation: `TauCeti.endAlgEquivOfSimple`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Preadditive/Schur.html#TauCeti.endAlgEquivOfSimple)
- [Source of `TauCeti.endAlgEquivOfSimple` in TauCeti/CategoryTheory/Preadditive/Schur.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Preadditive/Schur.lean#L65)
