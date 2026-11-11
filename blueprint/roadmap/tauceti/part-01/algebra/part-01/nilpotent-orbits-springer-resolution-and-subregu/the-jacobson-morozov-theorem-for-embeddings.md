---
declaration: theorem
origin: cited
lean: TauCeti.exists_injective_lieHom_slFinTwo_iff
statement: formalized
proof: formalized
---

# The Jacobson–Morozov theorem for embeddings

In a Lie algebra with nondegenerate Killing
form over a field of characteristic zero, `e` is the image of the raising element `E₀₁` under an
injective Lie algebra homomorphism `sl (Fin 2) K →ₗ⁅K⁆ L` if and only if `e ≠ 0` and `ad e` is
nilpotent.

```lean
TauCeti.exists_injective_lieHom_slFinTwo_iff.{u_1, u_2} {K : Type u_1} {L : Type u_2} [Field K]
  [CharZero K] [LieRing L] [LieAlgebra K L] [LieAlgebra.IsKilling K L] {e : L} :
  (∃ φ, Function.Injective ⇑φ ∧ φ ((LieAlgebra.SpecialLinear.single 0 1 ⋯) 1) = e) ↔
    IsNilpotent ((LieAlgebra.ad K L) e) ∧ e ≠ 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Jacobson–Morozov theorem](the-jacobson-morozov-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_injective_lieHom_slFinTwo_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Sl2/Embedding.html#TauCeti.exists_injective_lieHom_slFinTwo_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_injective_lieHom_slFinTwo_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Sl2/Embedding.html#TauCeti.exists_injective_lieHom_slFinTwo_iff)
- [Source of `TauCeti.exists_injective_lieHom_slFinTwo_iff` in TauCeti/Algebra/Lie/Sl2/Embedding.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Lie/Sl2/Embedding.lean#L225)
- [Tau Ceti roadmap status: Nilpotent orbits, Springer resolution and subregular geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/NilpotentOrbits/STATUS.md)
