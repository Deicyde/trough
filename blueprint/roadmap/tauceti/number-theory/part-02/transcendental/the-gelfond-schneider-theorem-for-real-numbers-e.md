---
declaration: theorem
origin: cited
lean: TauCeti.transcendental_rpow
statement: formalized
proof: formalized
---

# The Gelfond–Schneider theorem for real numbers (Evertse, Theorem 4.21)

If `α > 0` and `β`
are real algebraic numbers with `α ≠ 1` and `β` irrational, then `α ^ β` is transcendental.

```lean
TauCeti.transcendental_rpow {α β : ℝ} (hα : IsAlgebraic ℚ α) (hβ : IsAlgebraic ℚ β) (h0 : 0 < α)
  (h1 : α ≠ 1) (hirr : Irrational β) : Transcendental ℚ (α ^ β)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Iterated Rolle's theorem](../../../analysis/part-01/calculus/part-01/iterated-rolles-theorem.md)
- [Liouville's inequality](../../part-01/diophantine-approximation-and-transcendence/part-01/liouvilles-inequality.md)
- [The Schwarz lemma on a grid of `p`-adic integers](../padics/the-schwarz-lemma-on-a-grid-of-p-adic-integers.md)
- [Siegel's lemma for a rational subspace, in the sup norm](../../part-01/heights-units-and-s-units-of-number-fields/part-02/siegels-lemma-for-a-rational-subspace-in-the-sup.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.transcendental_rpow`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/GelfondSchneider/Theorem.html#TauCeti.transcendental_rpow).

## Sources

- [Tau Ceti documentation: `TauCeti.transcendental_rpow`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/GelfondSchneider/Theorem.html#TauCeti.transcendental_rpow)
- [Source of `TauCeti.transcendental_rpow` in TauCeti/NumberTheory/Transcendental/GelfondSchneider/Theorem.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Transcendental/GelfondSchneider/Theorem.lean#L208)
