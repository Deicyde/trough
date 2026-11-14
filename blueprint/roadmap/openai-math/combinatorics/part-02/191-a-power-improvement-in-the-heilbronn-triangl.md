---
declaration: section
origin: cited
lean: OAI.Problem355.heilbronn_power_lower_bound, OAI.Problem355.almost_n_minus_two_refuted
statement: formalized
proof: formalized
---

# 191. A power improvement in the Heilbronn triangle lower bound

1 manuscript and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

For every sufficiently large *n*, constructs *n* points in the unit square such that every triangle has area at least $n^{-2+c}$ for one absolute *c* > 0. This disproves the conjectured almost-$n^{−2}$ upper bound in Heilbronn's triangle problem, which asks how large the smallest determined triangle can be.

## A power improvement in the Heilbronn triangle lower bound

There are absolute constants $\eta,c_1\gt 0$ such that, for every sufficiently large integer *n*, one can choose *n* points in the unit square so that every triangle they determine has area at least $c_1n^{-2+\eta}$. Thus the almost $n^{−2}$ upper-bound formulation of Heilbronn's triangle problem is false. The exponent *η* is fixed but extremely small.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-power-improvement-in-the-Heilbronn-triangle-lower-bound-September-25-2026/main.pdf); the Lean below formalizes results from it.

## The Lean formalization

Heilbronn's triangle problem asks how large the smallest triangle determined by $n$ points in the unit square can be. The formalization constructs an unbounded sequence of sizes $n$ and point sets for which every triangle has area at least $n^{-2+\eta}$, for one fixed $\eta>0$. It consequently refutes the proposed upper bound of order $n^{-2+\varepsilon}$ for every $\varepsilon>0$. The linked construction is for an unbounded sequence of sizes; the paper's statement for every sufficiently large $n$ is broader.

## Lean: Power improvement for the smallest Heilbronn triangle

```lean
theorem heilbronn_power_lower_bound :
    0 < heilbronnExponent ∧ ∃ n : ℕ → ℕ, ∃ P : ℕ → Finset Point,
      Filter.Tendsto n Filter.atTop Filter.atTop ∧ ∀ j : ℕ,
        3 ≤ n j ∧ (P j).card = n j ∧ pointsInUnitSquare (P j) ∧
        triangleAreasAtLeast (P j)
          (Real.rpow (n j : ℝ) (-2 + heilbronnExponent))
```

Stated in [HeilbronnTriangle.lean, line 51](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/HeilbronnTriangle.lean#L51). Proved in [lean/OAI/Geometry/HeilbronnTriangle/Main.lean, line 15](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/HeilbronnTriangle/Main.lean#L15).

```lean
theorem almost_n_minus_two_refuted :
    0 < heilbronnExponent / 2 ∧
      ¬ eventualAlmostUpperBound (heilbronnExponent / 2)
```

Stated in [HeilbronnTriangle.lean, line 59](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/HeilbronnTriangle.lean#L59). Proved in [lean/OAI/Geometry/HeilbronnTriangle/Main.lean, line 33](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/HeilbronnTriangle/Main.lean#L33).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/191.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/191.md)
