---
declaration: theorem
origin: cited
lean: TauCeti.not_infEquivAt_nat_int_sumLex_int
statement: formalized
proof: formalized
---

# Elementary equivalence is strictly weaker than infinitary equivalence

The countable
orders `ℤ` and `ℤ ⊕ₗ ℤ` are elementarily equivalent (`elementarilyEquivalent_int_sumLex_int`),
but some `L_{ω₁ω}` sentence distinguishes them. A fortiori they are not `L_{∞ω}`-equivalent, since
`TauCeti.InfEquivW.infEquivAt` turns `L_{∞ω}`-equivalence into agreement at `ℕ`.

```lean
TauCeti.not_infEquivAt_nat_int_sumLex_int : ¬TauCeti.InfEquivAt ℕ ℤ (ℤ ⊕ₗ ℤ)
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](firstorder-language-boundedformulainf.md)

## Proof depends on

- [Karp's theorem for countable structures](karps-theorem-for-countable-structures.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.not_infEquivAt_nat_int_sumLex_int`](https://taucetiproject.org/docs/TauCeti/ModelTheory/BackAndForth/DiscreteOrder.html#TauCeti.not_infEquivAt_nat_int_sumLex_int).

## Sources

- [Tau Ceti documentation: `TauCeti.not_infEquivAt_nat_int_sumLex_int`](https://taucetiproject.org/docs/TauCeti/ModelTheory/BackAndForth/DiscreteOrder.html#TauCeti.not_infEquivAt_nat_int_sumLex_int)
- [Source of `TauCeti.not_infEquivAt_nat_int_sumLex_int` in TauCeti/ModelTheory/BackAndForth/DiscreteOrder.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/ModelTheory/BackAndForth/DiscreteOrder.lean#L304)
- [Tau Ceti roadmap status: Infinitary syntax, back-and-forth, and Scott analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/InfinitaryLogic/STATUS.md)
