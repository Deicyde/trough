---
declaration: section
origin: cited
lean: Stacks.Examples.RadicalTower.fpqcTorsor_not_isomorphic_fppfTorsor
statement: formalized
proof: formalized
---

# 110.52 A torsor which is not an fppf torsor

Section 110.52 of the Stacks Project, [Tag 04AF](https://stacks.math.columbia.edu/tag/04AF). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 077B, a lemma

[Tag 077B](https://stacks.math.columbia.edu/tag/077B) in the Stacks Project.

**`Stacks.Examples.RadicalTower.fpqcTorsor_not_isomorphic_fppfTorsor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/GroupSchemes/PrincipalNotFppf/Torsor.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/GroupSchemes/PrincipalNotFppf/Torsor.lean#L222). The attribute's comment: “counterexample: for S = Spec ℚ and G = ∏ᵢ μ_{i+2} a principal homogeneous G-space is exhibited that is isomorphic to no fppf G-torsor, which is the failure of essential surjectivity the source's proof invokes; the two stacks G-Principal and G-Torsors are not themselves constructed here”.

> **Stacks Project, Tag 077B.**  Over `S = Spec ℚ` the group scheme `G = ∏ᵢ μ_{i+2}` has a
> principal homogeneous space, namely `P = Spec ℚ[x₀, x₁, …]/(xᵢ ^ (i + 2) - 2)`, which is
> isomorphic to no fppf `G`-torsor.  Hence the inclusion of the fppf `G`-torsors into the
> principal homogeneous `G`-spaces is not essentially surjective, so the two stacks they form are
> not equivalent in general.

```lean
theorem fpqcTorsor_not_isomorphic_fppfTorsor :
    IsFpqcTorsor base groupObj torsorObj ∧
      ∀ (Y : Over base) (_ : ModObj groupObj Y),
        IsFppfTorsor base groupObj Y → ¬ Nonempty (torsorObj ≅ Y)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.52, Tag 04AF](https://stacks.math.columbia.edu/tag/04AF)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
