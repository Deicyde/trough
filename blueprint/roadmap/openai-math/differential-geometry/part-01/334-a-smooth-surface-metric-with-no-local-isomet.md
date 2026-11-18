---
declaration: section
origin: cited
lean: OAI.SmoothLocal.Geometry.exists_local_metric_without_local_immersion
statement: formalized
proof: formalized
---

# 334. A smooth surface metric with no local isometric immersion in ℝ$^{3}$

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Constructs a smooth positive-definite metric on $(-1,1)^2$ for which no neighborhood of the origin admits a smooth isometric immersion into ℝ$^{3}$. This answers the unrestricted smooth local isometric realization problem for surfaces negatively, even after shrinking the neighborhood.

## A Smooth Metric with No Local Isometric Immersion into Three-Space

We construct a smooth positive-definite Riemannian metric on $(-1,1)^2$ that agrees with the Euclidean metric to every order at the origin, yet no neighborhood of the origin admits a smooth isometric immersion into Euclidean three-space. This gives a negative answer to the unrestricted smooth local isometric realization problem for surfaces.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-Smooth-Metric-with-No-Local-Isometric-Immersion-into-Three-Space-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The local isometric-immersion problem asks whether every smooth surface metric can be realized locally in Euclidean three-space. The formalized counterexample is a smooth positive-definite metric on $(-1,1)^2$ for which no neighborhood of the origin admits a smooth isometric immersion into $\mathbb R^3$. The obstruction applies to every smooth candidate map on every such neighborhood.

## Lean: Smooth local isometric-immersion obstruction

```lean
theorem exists_local_metric_without_local_immersion :
    ∃ g : coordinateSquareOpen → Matrix (Fin 2) (Fin 2) ℝ,
      LocalSmoothPositive coordinateSquareOpen g ∧
      ∀ U : Opens Coord, ∀ hUS : (U : Set Coord) ⊆ square,
        (0 : Coord) ∈ U → ∀ F : U → Ambient,
          ¬ (ContMDiff 𝓘(ℝ, Coord) 𝓘(ℝ, Ambient) ∞ F ∧
            ∀ p : U, ∀ v w : Coord,
              (inner ℝ : Ambient → Ambient → ℝ) (mfderiv 𝓘(ℝ, Coord) 𝓘(ℝ, Ambient) F p v)
                (mfderiv 𝓘(ℝ, Coord) 𝓘(ℝ, Ambient) F p w) =
                  v ⬝ᵥ (g ⟨p, hUS p.property⟩ *ᵥ w))
```

Stated in [IsometricImmersion.lean, line 46](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/IsometricImmersion.lean#L46). Proved in [lean/OAI/Geometry/IsometricImmersion/Main.lean, line 49](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/IsometricImmersion/Main.lean#L49). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/334.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/334.md)
