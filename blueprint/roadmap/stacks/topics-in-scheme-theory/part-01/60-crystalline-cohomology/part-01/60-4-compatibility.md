---
declaration: section
origin: cited
lean: Crystalline.DividedPowerRing.IsCompatible
statement: formalized
proof: formalized
---

# 60.4 Compatibility

Section 60.4 of the Stacks Project, [Tag 07HJ](https://stacks.math.columbia.edu/tag/07HJ). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07HK, a definition

[Tag 07HK](https://stacks.math.columbia.edu/tag/07HK) in the Stacks Project.

**`Crystalline.DividedPowerRing.IsCompatible`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Compatibility.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/Compatibility.lean#L46).

> Compatibility of the divided power structures of `A` and `B` along `f`: both structures
> extend to one on the sum of the distinguished ideal of `B` and the extension of that of `A`.

```lean
public abbrev DividedPowerRing.IsCompatible
    (A : _root_.DividedPowerRing.{u}) (B : _root_.DividedPowerRing.{v})
    (f : A.carrier →+* B.carrier) : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 60.4, Tag 07HJ](https://stacks.math.columbia.edu/tag/07HJ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
