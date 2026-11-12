---
declaration: section
origin: cited
lean: OAI.Paper320.quantitative_separation
statement: formalized
proof: formalized
---

# 132. A superquadratic separation of sensitivity and block sensitivity

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Constructs total Boolean functions with block sensitivity $\mathop{\mathrm{bs}}\nolimits (f)\ge s(f)^\alpha$ for a fixed *α* > 2, disproving the quadratic strengthening of the Sensitivity Conjecture. Here $s(f)$ counts influential individual-bit flips, while block sensitivity allows disjoint groups of bits to change together.

## A superquadratic separation between sensitivity and block sensitivity

We disprove the quadratic strengthening of the Sensitivity Conjecture by constructing nonconstant total Boolean functions whose block sensitivity grows faster than any constant multiple of sensitivity squared. In fact, for some fixed *α* > 2, our examples have unbounded block sensitivity and satisfy $\mathop{\mathrm{bs}}\nolimits (f)\ge s(f)^\alpha$.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-superquadratic-separation-between-sensitivity-and-block-sensitivity-September-25-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalized result disproves a universal quadratic bound of block sensitivity by sensitivity for total Boolean functions. For every integer $d\ge1$, it constructs a nonconstant function with $\mathrm{bs}(f)/s(f)^2\ge2^d/(4(d+2)^2)$, making the ratio unbounded. The formalization also gives a fixed exponent $\alpha>2$ and a sequence with $s(f)^\alpha\le\mathrm{bs}(f,0)$ while the latter tends to infinity; here $\mathrm{bs}(f,0)$ is block sensitivity at the all-zero input.

## Lean: Superquadratic sensitivity separation

Stated in [SensitivitySeparation.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SensitivitySeparation.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem quantitative_separation (d : ℕ) (hd : 1 ≤ d) :
    ∃ (n : ℕ) (f : (Fin n → Bool) → Bool),
      0 < n ∧ f (fun _ => false) = false ∧
      (∃ x y : Fin n → Bool, f x ≠ f y) ∧
      (2 : ℝ) ^ d / (4 * ((d : ℝ) + 2) ^ 2) ≤
        (blockSensitivity f : ℝ) / (sensitivity f : ℝ) ^ 2
```

Proved in [lean/OAI/Combinatorics/Sensitivity/Separation.lean, line 12](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/Sensitivity/Separation.lean#L12).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/132.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/132.md)
