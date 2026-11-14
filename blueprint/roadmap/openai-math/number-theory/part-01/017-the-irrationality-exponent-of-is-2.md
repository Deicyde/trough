---
declaration: section
origin: cited
lean: OAI.PiExponent.main
statement: formalized
proof: formalized
---

# 017. The irrationality exponent of *π* is 2

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves that the irrationality exponent of *π* is exactly 2: for every *ε* > 0 and all sufficiently large denominators *q*, every rational $p/q$ satisfies $|\pi-p/q|\ge q^{-2-\varepsilon}$. This also proves convergence of the Flint–Hills series $\sum_{n\ge1}1/(n^3\sin^2 n)$, with angles in radians.

## The irrationality exponent of pi is 2

We prove the conjecture that the irrationality exponent of *π* is 2. As a consequence, the classical Flint–Hills series $\sum_{n\ge1}1/(n^3\sin^2 n)$ converges, with angles in radians.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves that the irrationality exponent of $\pi$ is exactly two. For every $\nu>2$, all sufficiently large positive denominators $q$ satisfy $|\pi-p/q|\ge q^{-\nu}$ for every integer numerator $p$. It also states the exact supremum characterization using infinitely many rational approximations.

The paper's convergence consequence for the Flint–Hills series is outside this selected statement.

## Lean: The irrationality exponent of $\pi$ equals two

```lean
theorem main :
  (∀ ν : ℝ, 2 < ν → ∃ Q : ℤ, 2 ≤ Q ∧
    ∀ p q : ℤ, Q ≤ q →
      (q : ℝ) ^ (-ν) ≤ |Real.pi - (p : ℝ) / (q : ℝ)|) ∧
  sSup {ν : ℝ | 0 < ν ∧
    Set.Infinite {r : ℚ | 2 ≤ r.den ∧
      0 < |Real.pi - (r : ℝ)| ∧
      |Real.pi - (r : ℝ)| < (r.den : ℝ) ^ (-ν)}} = 2
```

Stated in [PiExponent.lean, line 7](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/PiExponent.lean#L7). Proved in [lean/OAI/NumberTheory/PiExponent/Main.lean, line 17](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/PiExponent/Main.lean#L17).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/017.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/017.md)
