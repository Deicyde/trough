---
declaration: theorem
origin: cited
lean: TauCeti.ExactK0.closure_propClasses_eq_top
statement: formalized
proof: formalized
---

# The generating half of the resolution theorem

If every object of `C` admits a finite
`P`-resolution, then the classes of the objects satisfying `P` generate exact `K₀`.

```lean
TauCeti.ExactK0.closure_propClasses_eq_top.{w, v, u} {C : Type u} [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.Preadditive C] [CategoryTheory.Limits.HasZeroObject C]
  [CategoryTheory.Limits.HasBinaryBiproducts C] (E : TauCeti.ExactStructure C)
  (P : CategoryTheory.ObjectProperty C) [CategoryTheory.EssentiallySmall.{w, v, u} C]
  (h : ∀ (X : C), E.admitsFiniteResolution P X) :
  AddSubgroup.closure (TauCeti.ExactK0.propClasses E P) = ⊤
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ExactK0.closure_propClasses_eq_top`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/GrothendieckGroup/Resolution.html#TauCeti.ExactK0.closure_propClasses_eq_top).

## Sources

- [Tau Ceti documentation: `TauCeti.ExactK0.closure_propClasses_eq_top`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/GrothendieckGroup/Resolution.html#TauCeti.ExactK0.closure_propClasses_eq_top)
- [Source of `TauCeti.ExactK0.closure_propClasses_eq_top` in TauCeti/CategoryTheory/GrothendieckGroup/Resolution.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/CategoryTheory/GrothendieckGroup/Resolution.lean#L339)
