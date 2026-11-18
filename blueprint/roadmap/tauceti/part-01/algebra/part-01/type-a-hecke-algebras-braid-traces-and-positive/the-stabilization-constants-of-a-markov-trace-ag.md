---
declaration: theorem
origin: cited
lean: TauCeti.InfiniteTypeAHeckeAlgebra.IsMarkovTrace.map_hyperbolicGen_eq_map_inv_iff
statement: formalized
proof: formalized
---

# The stabilization constants of a Markov trace agree exactly at `η = (1 - tanh α * tanh θ) / 2`

For a Markov trace with projection parameter `η` on the Hecke
algebra with parameter `q = exp (-θ)`, and `cosh α * cosh θ ≠ 0`, the traces of `γ n` and of
`γ n⁻¹` agree exactly when `η = (1 - tanh α * tanh θ) / 2`.

```lean
TauCeti.InfiniteTypeAHeckeAlgebra.IsMarkovTrace.map_hyperbolicGen_eq_map_inv_iff {α θ z η : ℂ}
  {τ : TauCeti.InfiniteTypeAHeckeAlgebra ℂ (TauCeti.hyperbolicHeckeParam θ) →ₗ[ℂ] ℂ}
  (hτ : TauCeti.InfiniteTypeAHeckeAlgebra.IsMarkovTrace z τ)
  (hz : z = Complex.exp (-θ) * η - Complex.exp θ * (1 - η)) (hα : Complex.cosh α ≠ 0)
  (hθ : Complex.cosh θ ≠ 0) (n : ℕ) :
  τ ↑(TauCeti.InfiniteTypeAHeckeAlgebra.hyperbolicGen α θ n) =
      τ ↑(TauCeti.InfiniteTypeAHeckeAlgebra.hyperbolicGen α θ n)⁻¹ ↔
    η = (1 - Complex.tanh α * Complex.tanh θ) / 2
```

## Depends on

- [TauCeti.InfiniteTypeAHeckeAlgebra](tauceti-infinitetypeaheckealgebra.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.InfiniteTypeAHeckeAlgebra.IsMarkovTrace.map_hyperbolicGen_eq_map_inv_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/Hyperbolic.html#TauCeti.InfiniteTypeAHeckeAlgebra.IsMarkovTrace.map_hyperbolicGen_eq_map_inv_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.InfiniteTypeAHeckeAlgebra.IsMarkovTrace.map_hyperbolicGen_eq_map_inv_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/Hyperbolic.html#TauCeti.InfiniteTypeAHeckeAlgebra.IsMarkovTrace.map_hyperbolicGen_eq_map_inv_iff)
- [Source of `TauCeti.InfiniteTypeAHeckeAlgebra.IsMarkovTrace.map_hyperbolicGen_eq_map_inv_iff` in TauCeti/Algebra/TypeAHeckeAlgebra/Hyperbolic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/TypeAHeckeAlgebra/Hyperbolic.lean#L305)
- [Tau Ceti roadmap status: Type-A Hecke algebras, braid traces, and positive quotients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TypeAHeckeAlgebras/STATUS.md)
