---
declaration: theorem
origin: cited
lean: TauCeti.ClassFieldTheory.sum_finiteHilbertInvariantAt_add_sum_infiniteHilbertInvariantAt_eq_zero_iff
statement: formalized
proof: formalized
---

# Quadratic reciprocity is Hilbert reciprocity for two odd primes

For distinct odd primes
`p` and `q`, the cohomological Hilbert invariants of `p` and `q` sum to zero over the places of
`ℚ` exactly when `(p / q) (q / p) = (-1) ^ ((p - 1)/2 · (q - 1)/2)`. So Hilbert's reciprocity law
`∑_v inv_v((p) ∪ (q)) = 0` gives the quadratic reciprocity law, its dyadic factor being the sign.

```lean
TauCeti.ClassFieldTheory.sum_finiteHilbertInvariantAt_add_sum_infiniteHilbertInvariantAt_eq_zero_iff
  {p q : ℕ} [Fact (Nat.Prime p)] [Fact (Nat.Prime q)] {a b : ℚˣ} (hp : p ≠ 2) (hq : q ≠ 2)
  (hpq : p ≠ q) (ha : ↑a = ↑p) (hb : ↑b = ↑q) :
  ∑ v ∈ TauCeti.ClassFieldTheory.finiteHilbertSupport ℚ a b,
          TauCeti.ClassFieldTheory.finiteHilbertInvariantAt ℚ v a b +
        ∑ w, TauCeti.ClassFieldTheory.infiniteHilbertInvariantAt ℚ w a b =
      0 ↔
    legendreSym q ↑p * legendreSym p ↑q = (-1) ^ (p / 2 * (q / 2))
```

## Depends on

- [The Kummer isomorphism `Kˣ ⧸ (Kˣ)ⁿ ≃* H¹(G_K, μₙ)` (NSW (6.2.1) and the display following it), for `n` invertible in `K`](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism-kx-kx-n-h1-g-k-n-nsw-6-2.md)
- [The local invariant `inv_K : Br K ≃+ ℚ/ℤ` of a nonarchimedean local field `K`, normalized by arithmetic Frobenius](the-local-invariant-inv-k-br-k-q-z-of-a-nonarchi.md)

## Proof depends on

- [Dedekind's different theorem, the tame case](../../part-02/local-field/dedekinds-different-theorem-the-tame-case.md)
- [Euler's theorem on an `n`-th root of unity](../../../group-theory/other-results/eulers-theorem-on-an-n-th-root-of-unity.md)
- [The first half of Dedekind's different theorem](../../part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)
- [Hensel's lemma with an estimate over a Henselian discrete valuation ring](../counting-totally-ramified-extensions-of-a-local/part-01/hensels-lemma-with-an-estimate-over-a-henselian.md)
- [Hilbert reciprocity](hilbert-reciprocity.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.sum_finiteHilbertInvariantAt_add_sum_infiniteHilbertInvariantAt_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/QuadraticReciprocity.html#TauCeti.ClassFieldTheory.sum_finiteHilbertInvariantAt_add_sum_infiniteHilbertInvariantAt_eq_zero_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.sum_finiteHilbertInvariantAt_add_sum_infiniteHilbertInvariantAt_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/QuadraticReciprocity.html#TauCeti.ClassFieldTheory.sum_finiteHilbertInvariantAt_add_sum_infiniteHilbertInvariantAt_eq_zero_iff)
- [Source of `TauCeti.ClassFieldTheory.sum_finiteHilbertInvariantAt_add_sum_infiniteHilbertInvariantAt_eq_zero_iff` in TauCeti/NumberTheory/ClassFieldTheory/Global/QuadraticReciprocity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ClassFieldTheory/Global/QuadraticReciprocity.lean#L181)
- [Tau Ceti roadmap status: Class field theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ClassFieldTheory/STATUS.md)
