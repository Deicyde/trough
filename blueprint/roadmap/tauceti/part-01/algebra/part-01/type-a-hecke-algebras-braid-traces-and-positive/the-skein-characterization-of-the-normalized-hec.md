---
declaration: theorem
origin: cited
lean: TauCeti.MarkovBraid.eq_heckeTrace_of_skein
statement: formalized
proof: formalized
---

# The skein characterization of the normalized Hecke trace

A Markov invariant `F`
satisfying the skein relation `l⁻¹ * F(σᵢ c) - l * F(σᵢ⁻¹ c) = (q - q⁻¹) * F(c)`, multiplied by
`C` when an uncrossed strand is added, and with value `1` on the unknot, is the normalized Hecke
trace. In particular this applies to the Ocneanu trace.

```lean
TauCeti.MarkovBraid.eq_heckeTrace_of_skein.{u_1} {R : Type u_1} [CommRing R] {q : Rˣ} {z : R}
  {τ : TauCeti.InfiniteTypeAHeckeAlgebra R q →ₗ[R] R} {l : Rˣ} {C : R}
  (hτ : TauCeti.InfiniteTypeAHeckeAlgebra.IsMarkovTrace z τ) (hpos : C * ↑l * z = 1)
  (hneg : C * ↑l⁻¹ * (z - (↑q - ↑q⁻¹)) = 1) {F : TauCeti.MarkovBraid → R}
  (hF : ∀ (β γ : TauCeti.MarkovBraid), TauCeti.MarkovEquiv β γ → F β = F γ)
  (hs :
    ∀ (n : ℕ) (c : TauCeti.BraidGroup (n + 1)) (i : Fin n),
      ↑l⁻¹ * F { predStrands := n, braid := TauCeti.BraidGroup.sigma i * c } -
          ↑l * F { predStrands := n, braid := (TauCeti.BraidGroup.sigma i)⁻¹ * c } =
        (↑q - ↑q⁻¹) * F { predStrands := n, braid := c })
  (hι :
    ∀ (n : ℕ) (b : TauCeti.BraidGroup (n + 1)),
      F { predStrands := n + 1, braid := TauCeti.BraidGroup.strandIncl b } =
        C * F { predStrands := n, braid := b })
  (h₁ : F { predStrands := 0, braid := 1 } = 1) : F = fun β => β.heckeTrace τ C l
```

## Depends on

- [TauCeti.InfiniteTypeAHeckeAlgebra](tauceti-infinitetypeaheckealgebra.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.MarkovBraid.eq_heckeTrace_of_skein`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Hecke.html#TauCeti.MarkovBraid.eq_heckeTrace_of_skein).

## Sources

- [Tau Ceti documentation: `TauCeti.MarkovBraid.eq_heckeTrace_of_skein`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Hecke.html#TauCeti.MarkovBraid.eq_heckeTrace_of_skein)
- [Source of `TauCeti.MarkovBraid.eq_heckeTrace_of_skein` in TauCeti/KnotTheory/Hecke.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/KnotTheory/Hecke.lean#L45)
- [Tau Ceti roadmap status: Type-A Hecke algebras, braid traces, and positive quotients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TypeAHeckeAlgebras/STATUS.md)
