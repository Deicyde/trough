---
declaration: theorem
origin: cited
lean: TauCeti.GlobalNumberFields.infiniteAdeleSemilocalEquiv_infiniteAdeleGaloisAction
statement: formalized
proof: formalized
---

# The Galois action on the semi-local decomposition

Under `infiniteAdeleSemilocalEquiv`,
the Galois action of `σ ∈ Aut(L/K)` on infinite adeles applies the base change `id ⊗ σ` to each
semi-local factor `K_v ⊗[K] L`.

```lean
TauCeti.GlobalNumberFields.infiniteAdeleSemilocalEquiv_infiniteAdeleGaloisAction.{u_1, u_2}
  {K : Type u_1} [Field K] [NumberField K] {L : Type u_2} [Field L] [NumberField L] [Algebra K L]
  (σ : Gal(L/K)) (a : NumberField.InfiniteAdeleRing L) (v : NumberField.InfinitePlace K) :
  (TauCeti.GlobalNumberFields.infiniteAdeleSemilocalEquiv K L)
      (((TauCeti.GlobalNumberFields.infiniteAdeleGaloisAction K L) σ) a) v =
    ((TauCeti.Algebra.TensorProduct.baseChangeAutHom v.Completion L) σ)
      ((TauCeti.GlobalNumberFields.infiniteAdeleSemilocalEquiv K L) a v)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GlobalNumberFields.infiniteAdeleSemilocalEquiv_infiniteAdeleGaloisAction`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/LocalGlobal/Semilocal/InfiniteAdele.html#TauCeti.GlobalNumberFields.infiniteAdeleSemilocalEquiv_infiniteAdeleGaloisAction).

## Sources

- [Tau Ceti documentation: `TauCeti.GlobalNumberFields.infiniteAdeleSemilocalEquiv_infiniteAdeleGaloisAction`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/LocalGlobal/Semilocal/InfiniteAdele.html#TauCeti.GlobalNumberFields.infiniteAdeleSemilocalEquiv_infiniteAdeleGaloisAction)
- [Source of `TauCeti.GlobalNumberFields.infiniteAdeleSemilocalEquiv_infiniteAdeleGaloisAction` in TauCeti/NumberTheory/NumberField/LocalGlobal/Semilocal/InfiniteAdele.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/NumberField/LocalGlobal/Semilocal/InfiniteAdele.lean#L227)
