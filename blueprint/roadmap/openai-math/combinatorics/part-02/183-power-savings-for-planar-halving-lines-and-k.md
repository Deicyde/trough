---
declaration: section
origin: cited
lean: OAI.PlanarHalving.power_bounds
statement: formalized
proof: formalized
---

# 183. Power savings for planar halving lines and *k*-sets

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Improves the planar halving-line bound to $O(n^{4/3-\varepsilon})$ for sets with no three collinear and an absolute *ε* > 0. More generally, an *n*-point set with no three collinear has $O(n(k+1)^{1/3-\varepsilon_0})$ strictly separable *k*-subsets for $1\le k\le n/2$, with an absolute $\varepsilon_0\gt 0$. The constants and positive exponents are nonquantitative.

## A power saving for planar halving lines

There are absolute constants *ε* > 0 and *C* such that every sufficiently large even *n*-point set in the plane with no three collinear has at most $Cn^{4/3-\varepsilon}$ unordered halving pairs. This gives a power saving over the classical $O(n^{4/3})$ bound for planar halving lines. The proof is nonquantitative and does not supply explicit constants.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-power-saving-for-planar-halving-lines-September-25-2026/main.pdf); the Lean below formalizes results from it.

## The Lean formalization

A halving pair in an even planar point set is a pair whose line leaves equally many remaining points on each side. The formalization proves that some absolute $\varepsilon>0$ and $C$ bound the number of halving pairs by $Cn^{4/3-\varepsilon}$ for every sufficiently large even $n$ and every $n$-point set with no three collinear. It also proves a bound of the same form for all level-switch counts under the additional generic-position assumptions in the statement. The constants are existential.

## Lean: Power-saving bounds for halving pairs and level switches

```lean
theorem power_bounds :
    (∃ ε : ℝ, 0 < ε ∧ ∃ C : ℝ, ∃ n₀ : ℕ,
      ∀ n : ℕ, Even n → n₀ ≤ n → ∀ P : Fin n → Point,
        GeneralPosition P → (halvingCount P : ℝ) ≤ C * (n : ℝ) ^ ((4 : ℝ) / 3 - ε)) ∧
    (∃ ε : ℝ, 0 < ε ∧ ∃ C : ℝ,
      ∀ n : ℕ, 1 ≤ n → ∀ P : Fin n → Point, Generic P →
        ∀ k : ℕ, k ≤ n → (switchCount P k : ℝ) ≤ C * (n : ℝ) ^ ((4 : ℝ) / 3 - ε))
```

Stated in [HalvingLines.lean, line 45](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/HalvingLines.lean#L45). Proved in [lean/OAI/Combinatorics/HalvingLines/Main.lean, line 27](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/HalvingLines/Main.lean#L27).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/183.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/183.md)
