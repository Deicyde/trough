---
declaration: section
origin: cited
lean: OAI.KirchbergRordam.character_criterion
statement: formalized
proof: formalized
---

# 299. The Kirchberg–Rørdam character criterion and infinite tensor-power Jiang–Su stability

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

A nonzero unital separable complex $C^{∗}$-algebra is Jiang–Su stable exactly when its norm central-sequence algebra has no characters, for every free ultrafilter. This answers the Kirchberg–Rørdam character question. Also, the infinite minimal tensor power of every such algebra without characters is Jiang–Su stable, answering the Dadarlat–Toms question.

## The Kirchberg–Rørdam character criterion

We prove the Kirchberg–Rørdam character criterion: for every free ultrafilter on ℕ, a nonzero unital separable complex $C^{∗}$-algebra absorbs the Jiang–Su algebra if and only if its norm central-sequence algebra has no characters. We also prove that the infinite minimal tensor power of every nonzero unital separable complex $C^{∗}$-algebra without characters is $\mathcal Z$-stable and contains a unital copy of $\mathcal Z$.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-Kirchberg-Rordam-character-criterion-September-25-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The Kirchberg–Rørdam criterion relates Jiang–Su absorption to characters of the central-sequence algebra. The formalized result proves that, for every nonzero unital separable complex $C^*$-algebra $A$ and every free ultrafilter on $\mathbb N$, the norm central-sequence algebra has no nonzero character exactly when $A\cong A\otimes_{\min}\mathcal Z$. No nuclearity, simplicity, trace, or comparison hypothesis is imposed.

## Lean: Kirchberg–Rørdam character criterion

Stated in [CharacterCriterion.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/CharacterCriterion.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem character_criterion
    (A : Type) [CStarAlgebra A] [Nontrivial A] [TopologicalSpace.SeparableSpace A]
    (ω : Ultrafilter ℕ) (hω : (ω : Filter ℕ)≤Filter.cofinite) :
    OAI.KirchbergRordam.HasNoCharacters (NormUltrapower.CentralAlgebra A ω) ↔
      Nonempty (A ≃⋆ₐ[ℂ] MinTensor.Algebra A JiangSu.Algebra)
```

Proved in [lean/OAI/Analysis/CharacterCriterion/Main.lean, line 52](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/CharacterCriterion/Main.lean#L52).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/299.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/299.md)
