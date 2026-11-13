---
declaration: theorem
origin: cited
lean: Mathoverflow31809.mathoverflow_31809
statement: formalized
---

# Mathoverflow 31809

> Source:
> [Mathoverflow/31809](https://mathoverflow.net/questions/31809/pre-triangulated-category-that-isnt-triangulated)
>
> *References:*
> - [CLLZ26] X.-W. Chen, J. Liu, X.-S. Lu and C. Zhang, "A pre-triangulated category which is not
>   triangulated", [arXiv:2608.09777](https://arxiv.org/abs/2608.09777)

*Quoted from [FormalConjectures/Mathoverflow/31809.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Mathoverflow/31809.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `Mathoverflow31809.mathoverflow_31809`

Solved: stated here without proof.

> Does there exist a category that is pretriangulated but not triangulated?
>
> Yes. Theorem 1.2 of [CLLZ26] twists the triangulated structure on the category of finitely
> generated projective modules over the preprojective algebra of type $A_5$ over $\mathbb{F}_2$.
> The result is pretriangulated but does not satisfy the octahedral axiom.

```lean
theorem mathoverflow_31809 : ¬ (∀ (C : Type*) [Category C] [Preadditive C]
    [HasZeroObject C] [HasShift C ℤ] [∀ (n : ℤ), (shiftFunctor C n).Additive]
    [Pretriangulated C], IsTriangulated C)
```

Category `research solved`; AMS [18 Category theory; homological algebra](../by-subject/part-01/18-category-theory-homological-algebra/README.md). Declared in [FormalConjectures/Mathoverflow/31809.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Mathoverflow/31809.lean#L44).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Mathoverflow/31809.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Mathoverflow/31809.lean)
- [arXiv:2608.09777](https://arxiv.org/abs/2608.09777)
