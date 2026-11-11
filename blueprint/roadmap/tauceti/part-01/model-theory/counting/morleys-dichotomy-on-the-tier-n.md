---
declaration: theorem
origin: cited
lean: TauCeti.mk_quotient_isoSetoidOn_nat_le_aleph_one_or_hasPerfectAntichainOn, TauCeti.mk_isoClasses_le_aleph_one_or_hasPerfectAntichainOn
statement: formalized
proof: formalized
---

# Morley's dichotomy on the tier `ℕ`

In a relational language with countably many relation
symbols of each arity, the models on `ℕ` of an infinitary sentence with countable branching have at
most `ℵ₁` isomorphism classes, or contain a nonempty perfect set of pairwise non-isomorphic
models.

```lean
TauCeti.mk_quotient_isoSetoidOn_nat_le_aleph_one_or_hasPerfectAntichainOn.{u, v, uι}
  {L : FirstOrder.Language} [L.IsRelational] {ι : Type uι} [∀ (n : ℕ), Countable (L.Relations n)]
  [Countable ι] (φ : L.SentenceInf ι) :
  Cardinal.mk (Quotient (TauCeti.RelationalConfiguration.isoSetoidOn ℕ φ)) ≤ Cardinal.aleph 1 ∨
    (TauCeti.RelationalConfiguration.isoSetoid L ℕ).HasPerfectAntichainOn
      (TauCeti.RelationalConfiguration.modelsOf φ)
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](../infinitary-syntax-back-and-forth-and-scott-analy/firstorder-language-boundedformulainf.md)

## Proof depends on

- [Setoid.HasCantorAntichainOn](../../set-theory/borel-equivalence-relations-the-g0-dichotomy-and/setoid-hascantorantichainon.md)
- [Silver's theorem relative to a Borel subset](../../set-theory/borel-equivalence-relations-the-g0-dichotomy-and/silvers-theorem-relative-to-a-borel-subset.md)
- [The stratification bound](../counting-countable-models-morleys-theorem-and-th/the-stratification-bound.md)
- [TauCeti.BFEquiv](../infinitary-syntax-back-and-forth-and-scott-analy/tauceti-bfequiv.md)
- [TauCeti.BFScattered](../counting-countable-models-morleys-theorem-and-th/tauceti-bfscattered.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.mk_quotient_isoSetoidOn_nat_le_aleph_one_or_hasPerfectAntichainOn`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Counting/Morley.html#TauCeti.mk_quotient_isoSetoidOn_nat_le_aleph_one_or_hasPerfectAntichainOn).

## Other forms

**Morley's dichotomy for Borel sets on `ℕ`.** Formalized in Tau Ceti as [`TauCeti.mk_isoClasses_le_aleph_one_or_hasPerfectAntichainOn`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Counting/Morley.html#TauCeti.mk_isoClasses_le_aleph_one_or_hasPerfectAntichainOn).

```lean
TauCeti.mk_isoClasses_le_aleph_one_or_hasPerfectAntichainOn.{u, v} {L : FirstOrder.Language}
  [L.IsRelational] [∀ (n : ℕ), Countable (L.Relations n)]
  {K : Set (TauCeti.RelationalConfiguration L ℕ)} (hK : MeasurableSet K) :
  Cardinal.mk
        (Quotient (Setoid.comap Subtype.val (TauCeti.RelationalConfiguration.isoSetoid L ℕ))) ≤
      Cardinal.aleph 1 ∨
    (TauCeti.RelationalConfiguration.isoSetoid L ℕ).HasPerfectAntichainOn K
```

## Sources

- [Tau Ceti documentation: `TauCeti.mk_quotient_isoSetoidOn_nat_le_aleph_one_or_hasPerfectAntichainOn`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Counting/Morley.html#TauCeti.mk_quotient_isoSetoidOn_nat_le_aleph_one_or_hasPerfectAntichainOn)
- [Source of `TauCeti.mk_quotient_isoSetoidOn_nat_le_aleph_one_or_hasPerfectAntichainOn` in TauCeti/ModelTheory/Counting/Morley.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/ModelTheory/Counting/Morley.lean#L129)
