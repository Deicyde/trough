---
declaration: theorem
origin: cited
lean: TauCeti.existsUnique_lie_eq_and_lie_eq_neg_two_nsmul, TauCeti.existsUnique_isSl2Triple_of_isNilpotent_ad
statement: formalized
proof: formalized
---

# Morozov's lemma

Let `ad e` be nilpotent, `⁅h, e⁆ = 2 • e` and `h ∈ [e, L]`, over a field
of characteristic zero. Then there is a unique `f` with `⁅e, f⁆ = h` and `⁅h, f⁆ = -(2 • f)`.
The case `h = 0` is allowed.

```lean
TauCeti.existsUnique_lie_eq_and_lie_eq_neg_two_nsmul.{u_1, u_2} {K : Type u_1} {L : Type u_2}
  [Field K] [CharZero K] [LieRing L] [LieAlgebra K L] {h e : L}
  (he : IsNilpotent ((LieAlgebra.ad K L) e)) (hhe : ⁅h, e⁆ = 2 • e)
  (hh : h ∈ LinearMap.range ((LieAlgebra.ad K L) e)) : ∃! f, ⁅e, f⁆ = h ∧ ⁅h, f⁆ = -(2 • f)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.existsUnique_lie_eq_and_lie_eq_neg_two_nsmul`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Sl2/Morozov.html#TauCeti.existsUnique_lie_eq_and_lie_eq_neg_two_nsmul).

## Other forms

**Morozov's lemma for `sl₂` triples.** Formalized in Tau Ceti as [`TauCeti.existsUnique_isSl2Triple_of_isNilpotent_ad`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Sl2/Morozov.html#TauCeti.existsUnique_isSl2Triple_of_isNilpotent_ad).

```lean
TauCeti.existsUnique_isSl2Triple_of_isNilpotent_ad.{u_1, u_2} {K : Type u_1} {L : Type u_2}
  [Field K] [CharZero K] [LieRing L] [LieAlgebra K L] {h e : L}
  (he : IsNilpotent ((LieAlgebra.ad K L) e)) (hhe : ⁅h, e⁆ = 2 • e)
  (hh : h ∈ LinearMap.range ((LieAlgebra.ad K L) e)) (h0 : h ≠ 0) : ∃! f, IsSl2Triple h e f
```

## Sources

- [Tau Ceti documentation: `TauCeti.existsUnique_lie_eq_and_lie_eq_neg_two_nsmul`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Sl2/Morozov.html#TauCeti.existsUnique_lie_eq_and_lie_eq_neg_two_nsmul)
- [Source of `TauCeti.existsUnique_lie_eq_and_lie_eq_neg_two_nsmul` in TauCeti/Algebra/Lie/Sl2/Morozov.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Lie/Sl2/Morozov.lean#L212)
