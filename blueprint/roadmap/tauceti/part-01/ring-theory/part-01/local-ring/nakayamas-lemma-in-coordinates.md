---
declaration: theorem
origin: cited
lean: TauCeti.maximalIdeal_eq_span_range_of_span_eq_top
statement: formalized
proof: formalized
---

# Nakayama's lemma in coordinates

Elements of `𝔪` whose gradients span `κⁿ` generate
`𝔪`.

```lean
TauCeti.maximalIdeal_eq_span_range_of_span_eq_top.{u_1, u_2, u_3, u_4} {R : Type u_1} {Q : Type u_2}
  {ι : Type u_3} {κ : Type u_4} [CommSemiring R] [CommRing Q] [Algebra R Q] [IsLocalRing Q]
  [DecidableEq ι] {x : ι → Q} {D : ι → Derivation R Q Q} [Finite ι] [Finite κ]
  (hx : IsLocalRing.maximalIdeal Q = Ideal.span (Set.range x))
  (hD : ∀ (i j : ι), (D i) (x j) = if i = j then 1 else 0) {w : κ → Q}
  (hw : ∀ (k : κ), w k ∈ IsLocalRing.maximalIdeal Q)
  (h :
    Submodule.span (IsLocalRing.ResidueField Q)
        (Set.range fun k i => (IsLocalRing.residue Q) ((D i) (w k))) =
      ⊤) :
  IsLocalRing.maximalIdeal Q = Ideal.span (Set.range w)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.maximalIdeal_eq_span_range_of_span_eq_top`](https://taucetiproject.org/docs/TauCeti/RingTheory/LocalRing/Coordinates.html#TauCeti.maximalIdeal_eq_span_range_of_span_eq_top).

## Sources

- [Tau Ceti documentation: `TauCeti.maximalIdeal_eq_span_range_of_span_eq_top`](https://taucetiproject.org/docs/TauCeti/RingTheory/LocalRing/Coordinates.html#TauCeti.maximalIdeal_eq_span_range_of_span_eq_top)
- [Source of `TauCeti.maximalIdeal_eq_span_range_of_span_eq_top` in TauCeti/RingTheory/LocalRing/Coordinates.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/LocalRing/Coordinates.lean#L151)
