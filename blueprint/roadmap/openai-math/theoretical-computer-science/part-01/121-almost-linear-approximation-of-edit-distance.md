---
declaration: section
origin: cited
lean: OAI.EditApproximation.almostLinearEditDistanceRawBand
statement: formalized
proof: formalized
---

# 121. Almost-linear approximation of edit distance

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

For every fixed rational $\varepsilon\in(0,1)$, gives a randomized $(1+\varepsilon)$ approximation to unit-cost edit distance in worst-case expected time $N^{1+o(1)}$, with success probability at least 2/3. The strings have total length *N* and polynomially bounded integer symbols. This is an asymptotic guarantee at fixed accuracy.

## An Almost-Linear Approximation Scheme for Edit Distance

We give a uniform randomized approximation scheme for unit-cost edit distance. For every fixed rational $\varepsilon\in(0,1)$, it estimates the distance between arbitrary explicitly stored strings of total length *N* within a factor $1+\varepsilon$ with probability at least 2/3, in worst-case expected time $N^{1+o(1)}$ on a logarithmic-word RAM. The algorithm supports polynomially bounded integer alphabets and returns zero deterministically on equal strings.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/An-Almost-Linear-Approximation-Scheme-for-Edit-Distance-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization gives a randomized $(1+\varepsilon)$-approximation for unit-cost edit distance between explicitly stored integer strings, for every fixed rational $0<\varepsilon<1$. Its estimate is at least the true distance and at most $(1+\varepsilon)$ times it with probability at least $2/3$; equal strings return zero on every execution.

For total length at most $N$ and integer symbols bounded by a fixed polynomial in $N$, expected work is at most $(N+2)^{1+\eta}$ for every fixed $\eta>0$ and all sufficiently large $N$. Space is polynomially bounded on every execution.

## Lean: Almost-linear randomized approximation of edit distance

```lean
theorem almostLinearEditDistanceRawBand (epsilon : OAI.EditApproximation.BinaryFraction)
    (hepsilon : 0 < epsilon.value) (_hepsilonOne : epsilon.value < 1)
    :
    (∀ (source target : List ℤ) (N : ℕ), source.length + target.length ≤ N →
      (2 / 3 : ℝ) ≤ (OAI.EditApproximation.computedFullLaw (source.map OAI.EditApproximation.integerSymbolCode) (target.map OAI.EditApproximation.integerSymbolCode) N epsilon).real
        {outcome | EditDistortion.edit source target ≤ OAI.EditApproximation.integerBinaryAnswerRawBand source target N epsilon outcome ∧
          (OAI.EditApproximation.integerBinaryAnswerRawBand source target N epsilon outcome : ℝ) ≤
            (1 + (epsilon.value : ℝ)) * OAI.EditDistortion.edit source target}) ∧
    (∀ (source target : List ℤ) (N : ℕ), source = target → ∀ outcome,
      OAI.EditApproximation.integerBinaryAnswerRawBand source target N epsilon outcome = 0) ∧
    (∀ (C : ℕ) (eta : ℝ), 0 < eta → ∀ᶠ N : ℕ in atTop,
      ∀ source target : List ℤ, source.length + target.length ≤ N →
        (∀ z ∈ source ++ target, z.natAbs ≤ (N + 2) ^ C) →
        (∫ outcome, OAI.EditApproximation.integerBinaryWorkRawBand source target N epsilon outcome
          ∂OAI.EditApproximation.computedFullLaw (source.map OAI.EditApproximation.integerSymbolCode) (target.map OAI.EditApproximation.integerSymbolCode) N epsilon) ≤
            (N + 2 : ℝ) ^ (1 + eta)) ∧
    (∀ C : ℕ, ∀ᶠ N : ℕ in atTop, ∀ source target : List ℤ,
      source.length + target.length ≤ N →
        (∀ z ∈ source ++ target, z.natAbs ≤ (N + 2) ^ C) →
        ∀ outcome, OAI.EditApproximation.integerBinarySpaceFootprintRawBand source target N epsilon outcome ≤ (N + 2) ^ (C + 65564))
```

Stated in [EditApproximation.lean, line 19146](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/EditApproximation.lean#L19146). Proved in [lean/OAI/Combinatorics/EditApproximation/Specification/RawBandMain.lean, line 8](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/EditApproximation/Specification/RawBandMain.lean#L8).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/121.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/121.md)
