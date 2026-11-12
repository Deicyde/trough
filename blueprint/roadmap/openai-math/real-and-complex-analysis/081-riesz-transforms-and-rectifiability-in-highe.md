---
declaration: section
origin: cited
lean: OAI.RieszRectifiability.quantitative_higher_codimension_riesz_rectifiability
statement: formalized
proof: formalized
---

# 081. Riesz transforms and rectifiability in higher codimension

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Resolves the remaining higher-codimension Riesz-transform rectifiability problem: for *d* ≥ 4 and $2\le n\le d-2$, an *n*-Ahlfors–David regular Radon measure on ℝ$^{d}$ is uniformly *n*-rectifiable whenever its *n*-dimensional Riesz transform is uniformly $L^{2}$-bounded over all positive hard truncations. The rectifiability bounds depend only on dimension, regularity and operator bounds.

## Riesz transforms and uniform rectifiability in higher codimension

We prove that an *n*-Ahlfors–David regular Radon measure on ℝ$^{d}$ is uniformly *n*-rectifiable if its *n*-dimensional Riesz transform is uniformly bounded from scalar $L^2(\mu)$ to vector-valued $L^2(\mu)$ over all positive hard truncations, for integers *d* ≥ 4 and $2\le n\le d-2$. This gives a positive answer to the David–Semmes Riesz-transform question in its remaining higher-codimension range. The conclusion gives uniform big pieces of Lipschitz images of Euclidean balls.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Riesz-transforms-and-uniform-rectifiability-in-higher-codimension-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalized result proves that bounded Riesz transforms force quantitative uniform rectifiability in higher codimension. For $d\ge4$ and $2\le n\le d-2$, an $n$-Ahlfors–David regular measure whose positive hard truncations have one uniform $L^2$ operator bound has big pieces of Lipschitz images. The mass fraction and Lipschitz constant depend only on the dimensions and the stated regularity and operator bounds, and work at every support point and admissible radius, including unbounded support. The variation and principal-value corollary is not included.

## Lean: Quantitative higher-codimension Riesz rectifiability

Stated in [RieszQuantitative.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/RieszQuantitative.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem quantitative_higher_codimension_riesz_rectifiability : QuantitativeFullStatement
```

Proved in [lean/OAI/Analysis/RieszRectifiability/Uniformity/Rectifiability.lean, line 89](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/RieszRectifiability/Uniformity/Rectifiability.lean#L89).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/081.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/081.md)
