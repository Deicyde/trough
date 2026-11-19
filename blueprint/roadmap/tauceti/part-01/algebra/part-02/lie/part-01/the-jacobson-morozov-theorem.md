---
declaration: theorem
origin: cited
lean: TauCeti.exists_isSl2Triple_of_isNilpotent_ad, TauCeti.exists_injective_lieHom_slFinTwo_iff
statement: formalized
proof: formalized
---

# The Jacobson–Morozov theorem

In a Lie algebra with nondegenerate
Killing form over a field of characteristic zero, every nonzero `ad`-nilpotent element `e` is the
nilpositive element of an `sl₂` triple `(h, e, f)`.

```lean
TauCeti.exists_isSl2Triple_of_isNilpotent_ad.{u_1, u_2} {K : Type u_1} {L : Type u_2} [Field K]
  [CharZero K] [LieRing L] [LieAlgebra K L] [LieAlgebra.IsKilling K L] {e : L}
  (he : IsNilpotent ((LieAlgebra.ad K L) e)) (he0 : e ≠ 0) : ∃ h f, IsSl2Triple h e f
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Jacobson's lemma on commutators](../../../../linear-algebra/part-02/other-results/jacobsons-lemma-on-commutators.md)
- [Morozov's lemma](morozovs-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isSl2Triple_of_isNilpotent_ad`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Sl2/JacobsonMorozov.html#TauCeti.exists_isSl2Triple_of_isNilpotent_ad).

## Other forms

**The Jacobson–Morozov theorem for embeddings.** Formalized in Tau Ceti as [`TauCeti.exists_injective_lieHom_slFinTwo_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Sl2/Embedding.html#TauCeti.exists_injective_lieHom_slFinTwo_iff).

```lean
TauCeti.exists_injective_lieHom_slFinTwo_iff.{u_1, u_2} {K : Type u_1} {L : Type u_2} [Field K]
  [CharZero K] [LieRing L] [LieAlgebra K L] [LieAlgebra.IsKilling K L] {e : L} :
  (∃ φ, Function.Injective ⇑φ ∧ φ ((LieAlgebra.SpecialLinear.single 0 1 ⋯) 1) = e) ↔
    IsNilpotent ((LieAlgebra.ad K L) e) ∧ e ≠ 0
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isSl2Triple_of_isNilpotent_ad`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Sl2/JacobsonMorozov.html#TauCeti.exists_isSl2Triple_of_isNilpotent_ad)
- [Source of `TauCeti.exists_isSl2Triple_of_isNilpotent_ad` in TauCeti/Algebra/Lie/Sl2/JacobsonMorozov.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Lie/Sl2/JacobsonMorozov.lean#L83)
