---
declaration: section
origin: cited
lean: OAI.Problem310.dyadic_affine_avoidance
statement: formalized
proof: formalized
---

# 084. The geometric case of the Erdős similarity conjecture

2 manuscripts and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

For every fixed $q\in(0,1)$, constructs compact subsets of $[0,1]$ with measure arbitrarily close to one containing no translated and nontrivially dilated copy of $\{q^n:n\ge1\}$, with dilations of either sign. This resolves the geometric-progression case of the Erdős similarity conjecture for every ratio.

## The geometric case of the Erdős similarity conjecture

We prove the geometric-progression case of the Erdős similarity conjecture. For every fixed $q\in(0,1)$ and every $\eta\in(0,1)$, we construct a compact set $E_{q,\eta}\subseteq[0,1]$ of measure greater than $1-\eta$ containing no nontrivial affine copy of $\{q^n:n\ge1\}$, for any translation and either sign of nonzero dilation. The set may depend on *q*; the result makes no simultaneous assertion for different ratios.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-geometric-case-of-the-Erdos-similarity-conjecture-October-5-2026/geometric-erdos-similarity.pdf).

## The dyadic case of the Erdős similarity conjecture

We construct a compact subset of the unit interval, of measure arbitrarily close to one, that contains no affine copy of the dyadic sequence $\{2^{-n}:n\ge1\}$. The conclusion holds for every translation and every nonzero real dilation, of either sign, proving the dyadic case of the Erdős similarity conjecture.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-dyadic-case-of-the-Erdos-similarity-conjecture-September-25-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves the dyadic case of the Erdős similarity conjecture. For every $0<\eta<1$, it constructs a compact set $E\subset[0,1]$ of measure greater than $1-\eta$ that contains no affine copy of $\{2^{-n}:n\ge1\}$. Explicitly, for every translation $x$ and every nonzero real dilation $s$, some point $x+s2^{-n}$ lies outside $E$. Both signs of $s$ are included.

## Lean: Positive-measure avoidance of every affine dyadic sequence

```lean
theorem dyadic_affine_avoidance :
    ∀ η : ℝ, 0 < η → η < 1 → ∃ E : Set ℝ,
      E ⊆ Set.Icc (0 : ℝ) 1 ∧ IsCompact E ∧
      MeasureTheory.volume E > ENNReal.ofReal (1 - η) ∧
      ∀ x s : ℝ, s ≠ 0 → ∃ n : ℕ, 1 ≤ n ∧
        x + s * dyadicPoint n ∉ E
```

Stated in [DyadicAvoidance.lean, line 12](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/DyadicAvoidance.lean#L12). Proved in [lean/OAI/MeasureTheory/DyadicAvoidance/Main.lean, line 103](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/MeasureTheory/DyadicAvoidance/Main.lean#L103).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/084.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/084.md)
