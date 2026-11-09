---
declaration: theorem
origin: cited
lean: TauCeti.mk_quotient_isoSetoidOn_nat_le_aleph_one_or_eq_continuum, TauCeti.mk_isoClasses_le_aleph_one_or_eq_continuum
statement: formalized
proof: formalized
---

# Morley's cardinal dichotomy on the tier `ℕ`

In a relational language with countably many
relation symbols of each arity, the models of `φ` on `ℕ` have either at most `ℵ₁` or `𝔠` isomorphism
classes.

```lean
TauCeti.mk_quotient_isoSetoidOn_nat_le_aleph_one_or_eq_continuum.{u, v, uι}
  {L : FirstOrder.Language} [L.IsRelational] {ι : Type uι} [∀ (n : ℕ), Countable (L.Relations n)]
  [Countable ι] (φ : L.SentenceInf ι) :
  Cardinal.mk (Quotient (TauCeti.RelationalConfiguration.isoSetoidOn ℕ φ)) ≤ Cardinal.aleph 1 ∨
    Cardinal.mk (Quotient (TauCeti.RelationalConfiguration.isoSetoidOn ℕ φ)) = Cardinal.continuum
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](../infinitary-syntax-back-and-forth-and-scott-analy/firstorder-language-boundedformulainf.md)

## Proof depends on

- [Morley's dichotomy on the tier `ℕ`](morleys-dichotomy-on-the-tier-n.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.mk_quotient_isoSetoidOn_nat_le_aleph_one_or_eq_continuum`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Counting/Morley.html#TauCeti.mk_quotient_isoSetoidOn_nat_le_aleph_one_or_eq_continuum).

## Other forms

**Morley's cardinal dichotomy for Borel sets on `ℕ`.** Formalized in Tau Ceti as [`TauCeti.mk_isoClasses_le_aleph_one_or_eq_continuum`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Counting/Morley.html#TauCeti.mk_isoClasses_le_aleph_one_or_eq_continuum).

```lean
TauCeti.mk_isoClasses_le_aleph_one_or_eq_continuum.{u, v} {L : FirstOrder.Language} [L.IsRelational]
  [∀ (n : ℕ), Countable (L.Relations n)] {K : Set (TauCeti.RelationalConfiguration L ℕ)}
  (hK : MeasurableSet K) :
  Cardinal.mk
        (Quotient (Setoid.comap Subtype.val (TauCeti.RelationalConfiguration.isoSetoid L ℕ))) ≤
      Cardinal.aleph 1 ∨
    Cardinal.mk
        (Quotient (Setoid.comap Subtype.val (TauCeti.RelationalConfiguration.isoSetoid L ℕ))) =
      Cardinal.continuum
```

## Sources

- [Tau Ceti documentation: `TauCeti.mk_quotient_isoSetoidOn_nat_le_aleph_one_or_eq_continuum`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Counting/Morley.html#TauCeti.mk_quotient_isoSetoidOn_nat_le_aleph_one_or_eq_continuum)
- [Source of `TauCeti.mk_quotient_isoSetoidOn_nat_le_aleph_one_or_eq_continuum` in TauCeti/ModelTheory/Counting/Morley.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/ModelTheory/Counting/Morley.lean#L139)
