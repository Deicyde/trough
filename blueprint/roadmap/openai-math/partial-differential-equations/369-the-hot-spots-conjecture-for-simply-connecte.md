---
declaration: section
origin: cited
lean: OAI.StrictHotSpots.main_theorem
statement: formalized
proof: formalized
---

# 369. The hot spots conjecture for simply connected planar domains

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves a strict form of Burdzy's simply connected hot spots conjecture. On every smooth bounded simply connected planar domain, each nonzero eigenfunction for the first positive Neumann eigenvalue has no interior critical point, so all global extrema lie on the boundary. Eigenvalue multiplicity is allowed.

## Strict hot spots and absence of interior critical points on smooth simply connected planar domains

We prove the strict hot spots conjecture for smooth bounded simply connected planar domains. More precisely, every nonzero eigenfunction for the first positive Neumann eigenvalue has nonvanishing gradient in the interior, so all its global maxima and minima lie on the boundary. This holds even when the eigenvalue is multiple.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Strict-hot-spots-and-absence-of-interior-critical-points-on-smooth-simply-connected-planar-domains-September-24-2026/main.pdf); the Lean below formalizes results from it.

## The Lean formalization

The strict hot-spots conjecture asks whether extrema of a first nonconstant Neumann eigenfunction occur only on the boundary. The formalization proves the stronger interior statement on every nonempty smooth bounded simply connected planar domain: every nonzero eigenfunction in the first positive Neumann eigenspace has nonvanishing gradient throughout the interior. Consequently all global maxima and minima lie on the boundary. The conclusion applies to every eigenfunction even when the eigenvalue is multiple.

## Lean: Strict hot spots and absence of interior critical points

```lean
theorem main_theorem (Ω : Set Plane) (hΩ : AdmissibleDomain Ω)
    (u : Plane → ℝ) (hu : InFirstNeumannEigenspace Ω u)
    (hne : ∃ x ∈ Ω, u x ≠ 0) : MainConclusion Ω u
```

Stated in [HotSpots.lean, line 49](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/HotSpots.lean#L49). Proved in [lean/OAI/Analysis/HotSpots/Main.lean, line 78](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/HotSpots/Main.lean#L78).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/369.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/369.md)
