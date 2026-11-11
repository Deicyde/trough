---
declaration: theorem
origin: cited
lean: TauCeti.W1p.norm_mul_le
statement: formalized
proof: formalized
---

# The supercritical Sobolev multiplication estimate

The `W^{1,p}` norm of a product is at
most three times the operator norm of Morrey's embedding times the product of the norms of the
factors. The embedding norm is what enters because the only control on a factor outside `L^p` is
the supremum norm of its Morrey representative.

```lean
TauCeti.W1p.norm_mul_le.{u_1} {E : Type u_1} [MeasurableSpace E] [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [BorelSpace E] {mu : MeasureTheory.Measure E}
  [mu.IsAddHaarMeasure] {p : NNReal} [Fact (1 ≤ ↑p)] (hp : ↑(Module.finrank ℝ E) < p)
  (u v : ↥(TauCeti.W1p mu ⊤ ↑p)) :
  ‖TauCeti.W1p.mul hp u v‖ ≤ 3 * ‖TauCeti.W1p.morreyEmbedding hp‖ * ‖u‖ * ‖v‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hölder's bound on an average](../../../../measure-theory/integral/part-01/holders-bound-on-an-average.md)
- [Morrey's inequality](morreys-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.W1p.norm_mul_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/W1p/SupercriticalMultiplication.html#TauCeti.W1p.norm_mul_le).

## Sources

- [Tau Ceti documentation: `TauCeti.W1p.norm_mul_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/W1p/SupercriticalMultiplication.html#TauCeti.W1p.norm_mul_le)
- [Source of `TauCeti.W1p.norm_mul_le` in TauCeti/Analysis/Sobolev/W1p/SupercriticalMultiplication.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Sobolev/W1p/SupercriticalMultiplication.lean#L493)
