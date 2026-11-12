---
declaration: section
origin: cited
lean: OAI.ArnoldCounterexample.main
statement: formalized
proof: formalized
---

# 347. Counterexamples to stable-Morse and strong Arnold fixed-point bounds

5 manuscripts and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Disproves stable-Morse lower bounds for nondegenerate Hamiltonian fixed points: on simply connected closed Kähler manifolds of real dimension 22, the deficit below the stable Morse number is unbounded. A separate Hamiltonian diffeomorphism of the complex quadric threefold has exactly three fixed points, fewer than the four critical points required of every smooth function.

## Hamiltonian Fixed Points Below the Stable Morse Number in Dimension Twenty-Two

We disprove the stable Morse lower bound for nondegenerate Hamiltonian fixed points with examples in fixed real dimension twenty-two. For every integer *m* ≥ 1, we construct a simply connected closed Kähler manifold with stable Morse number $80+1968m$ and a Hamiltonian diffeomorphism with exactly $80+1952m$ fixed points, all nondegenerate and with contractible orbit loops. The deficit is therefore unbounded, and the fixed-point count is at most 127/128 of the stable Morse number.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/hamiltonian-fixed-points-below-stable-morse-number.pdf).

## Sharpness of the Cyclic Integral Floer Bound Below the Stable Morse Number

We construct a simply connected closed Kähler manifold of real dimension 3332 and minimal Chern number one whose Hamiltonian fixed-point count attains the cyclic integral Floer bound while falling below the stable Morse number. The Hamiltonian diffeomorphism has exactly $1\,872\,232$ fixed points, all nondegenerate and with contractible orbit loops, whereas the stable Morse number is $1\,872\,264$. Thus the stronger stable Morse bound fails by exactly 32, even when the cyclic integral bound is sharp.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026/sharp-cyclic-integral-floer-bound-below-stable-morse-number.pdf).

## Hamiltonian Fixed Points Below the Stable Morse Number

We disprove the stable Morse lower bound for nondegenerate Hamiltonian fixed points by constructing a simply connected closed Kähler manifold with sixteen fewer fixed points than its stable Morse number. All the corresponding periodic orbits are contractible. The construction combines a Hamiltonian involution with integral homology torsion at two different primes; its proof uses finite-dimensional Morse theory and complex blowups.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/paper.pdf).

## A nondegenerate counterexample to the Morse-number Arnold bound

We construct a smooth one-periodic Hamiltonian on a closed symplectic twelve-manifold whose time-one map has fewer fixed points than the manifold's ordinary Morse number. Every fixed point is nondegenerate and has a contractible Hamiltonian trajectory. This disproves the Morse-number form of the Arnold conjecture. The deficit can be arbitrarily large among twelve-dimensional examples.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026/paper.pdf).

## Three fixed points on the symplectic quadric threefold

We construct a smooth Hamiltonian diffeomorphism of the complex quadric threefold with exactly three fixed points, at least one of which is degenerate. The critical number and the unit-inclusive rational cup length of this manifold are both four. Thus the example disproves the unrestricted critical-number and rational cup-length forms of the Arnold conjecture.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The critical-number form of Arnold's fixed-point conjecture predicts at least as many fixed points as the minimum number of critical points of a smooth function. The formalized counterexample is a Hamiltonian diffeomorphism of the complex quadric threefold with exactly three fixed points, while every smooth function on that manifold has at least four critical points. At least one fixed point is degenerate. The separate nondegenerate Morse-number construction is not included.

## Lean: Three-fixed-point Arnold counterexample

Stated in [ArnoldCounterexample.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ArnoldCounterexample.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem main :
    ∃ φ : Q3 ≃ Q3, IsHamiltonian φ ∧ (fixedSet φ).encard = 3 ∧
      (3 : ℕ∞) < 4 ∧ 4 ≤ criticalNumber ∧ HasDegenerateFixedPoint φ
```

Proved in [lean/OAI/Geometry/Arnold/Main.lean, line 14](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/Arnold/Main.lean#L14).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/347.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/347.md)
