---
declaration: theorem
origin: cited
lean: TauCeti.numberField_CoefficientField
statement: formalized
proof: formalized
---

# The coefficient field of a newform of weight at least two is a number field

```lean
TauCeti.numberField_CoefficientField {N : ℕ} [NeZero N] {k : ℤ} (f : HeckeRing.GL2.Newform N k)
  (hk : 2 ≤ k) : NumberField ↥(TauCeti.CoefficientField f)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Classical Sturm bound for finite-index subgroups of `SL(2, ℤ)`](../../part-02/modular-forms/classical-sturm-bound-for-finite-index-subgroups.md)
- [The Main Lemma, per character (Miyake, Lemma 4.6.8; Diamond–Shurman, Theorem 5.7.1)](../../part-02/modular-forms/the-main-lemma-per-character-miyake-lemma-4-6-8.md)
- [Manin's lemma](../../part-02/modular-forms/manins-lemma.md)
- [The Petersson adjoint formula in the second argument](../../part-02/modular-forms/the-petersson-adjoint-formula-in-the-second-argu.md)
- [Shimura's commutativity criterion (Proposition 3.8 of \[Shimura\]\[shimura1971\])](../../part-02/hecke-ring/shimuras-commutativity-criterion-proposition-3-8.md)
- [Shimura's decomposition of a double coset into right cosets](../../part-02/hecke-ring/shimuras-decomposition-of-a-double-coset-into-ri.md)
- [Sturm bound for subgroups of `GL(2, ℝ)` of finite relative index in `SL(2, ℤ)` with discrete strict periods](../../part-02/modular-forms/sturm-bound-for-subgroups-of-gl-2-r-of-finite-re.md)
- [The third isomorphism theorem for coset spaces](../../../group-theory/other-results/the-third-isomorphism-theorem-for-coset-spaces.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.numberField_CoefficientField`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/Newforms/NumberField.html#TauCeti.numberField_CoefficientField).

## Sources

- [Tau Ceti documentation: `TauCeti.numberField_CoefficientField`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/Newforms/NumberField.html#TauCeti.numberField_CoefficientField)
- [Source of `TauCeti.numberField_CoefficientField` in TauCeti/NumberTheory/ModularForms/Newforms/NumberField.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ModularForms/Newforms/NumberField.lean#L156)
- [Tau Ceti roadmap status: Modular forms — Hecke theory, newforms, and L-functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ModularForms/STATUS.md)
