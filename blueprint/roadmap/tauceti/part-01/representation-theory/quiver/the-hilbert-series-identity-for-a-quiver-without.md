---
declaration: theorem
origin: cited
lean: TauCeti.mul_preprojectiveHilbertSeries_eq_one, TauCeti.mul_preprojectiveHilbertSeries_eq_one_of_two_mul_le_sum
statement: formalized
proof: formalized
---

# The Hilbert series identity for a quiver without sinks

If every vertex of `Q` is the tail
of an arrow and `A_{v,w} = #(w ⟶ v)` is the arrow-count matrix of the doubled quiver, then
`((1 + X²) I - X A) H = I` for the matrix Hilbert series `H` of `Π`.

```lean
TauCeti.mul_preprojectiveHilbertSeries_eq_one.{u, v, w} (k : Type w) {Q : Type u} [Field k]
  [Quiver Q] [Fintype Q] [(i j : Q) → Fintype (i ⟶ j)] (hQ : ∀ (u : Q), ∃ w, Nonempty (u ⟶ w))
  [DecidableEq Q] :
  ((1 + PowerSeries.X ^ 2) • 1 -
        PowerSeries.X •
          Matrix.of fun v w =>
            ↑(Fintype.card (Quiver.Symmetrify.of.obj w ⟶ Quiver.Symmetrify.of.obj v))) *
      TauCeti.preprojectiveHilbertSeries k Q =
    1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Koszul defect formula](the-koszul-defect-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.mul_preprojectiveHilbertSeries_eq_one`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Preprojective/HilbertSeries/ZigzagCartan.html#TauCeti.mul_preprojectiveHilbertSeries_eq_one).

## Other forms

**The Hilbert series identity for a quiver with a superadditive weight.** Formalized in Tau Ceti as [`TauCeti.mul_preprojectiveHilbertSeries_eq_one_of_two_mul_le_sum`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Preprojective/Koszul/Superadditive.html#TauCeti.mul_preprojectiveHilbertSeries_eq_one_of_two_mul_le_sum).

```lean
TauCeti.mul_preprojectiveHilbertSeries_eq_one_of_two_mul_le_sum.{u, v, w, u_1} (k : Type w)
  {Q : Type u} [Field k] [Quiver Q] [Fintype Q] [(i j : Q) → Fintype (i ⟶ j)] [DecidableEq Q]
  {S : Type u_1} [CommRing S] [LinearOrder S] [IsStrictOrderedRing S] {δ : Q → S}
  (hδ : ∀ (i : Q), 0 < δ i)
  (hδle : ∀ (i : Q), 2 * δ i ≤ ∑ j, ↑(Fintype.card (i ⟶ j) + Fintype.card (j ⟶ i)) * δ j) :
  ((1 + PowerSeries.X ^ 2) • 1 -
        PowerSeries.X •
          Matrix.of fun v w =>
            ↑(Fintype.card (Quiver.Symmetrify.of.obj w ⟶ Quiver.Symmetrify.of.obj v))) *
      TauCeti.preprojectiveHilbertSeries k Q =
    1
```

## Sources

- [Tau Ceti documentation: `TauCeti.mul_preprojectiveHilbertSeries_eq_one`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Preprojective/HilbertSeries/ZigzagCartan.html#TauCeti.mul_preprojectiveHilbertSeries_eq_one)
- [Source of `TauCeti.mul_preprojectiveHilbertSeries_eq_one` in TauCeti/RepresentationTheory/Quiver/Preprojective/HilbertSeries/ZigzagCartan.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Quiver/Preprojective/HilbertSeries/ZigzagCartan.lean#L117)
