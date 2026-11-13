---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.pushout_isPushout_algebraicSpaces
statement: formalized
proof: formalized
---

# 81.7 Pushouts along closed immersions and integral morphisms

Section 81.7 of the Stacks Project, [Tag 0GG2](https://stacks.math.columbia.edu/tag/0GG2). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0EDP, a lemma

[Tag 0EDP](https://stacks.math.columbia.edu/tag/0EDP) in the Stacks Project.

**`AlgebraicGeometry.Space.pushout_isPushout_algebraicSpaces`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/Schemes.lean, line 651](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/Schemes.lean#L651).

> **Stacks 0EDP.** In the standing situation of [Stacks Project, Tag 0ECI], the scheme pushout
> `Y ⨿_Z X` of [Stacks Project, Tag 0E25] is also a pushout in the category of algebraic spaces
> over `S`: the square formed by the four schemes and the four canonical morphisms, regarded
> through the Yoneda embedding as a square of algebraic spaces over `S`, is a pushout square.

```lean
theorem pushout_isPushout_algebraicSpaces :
    IsPushout
      (ObjectProperty.homMk (yoneda.map (fppfOverI s B hS hX hZ)) :
        (⟨yoneda.obj (fppfOverZ s B hS hZ),
          isAlgebraicSpace_yoneda B s.S hS (fppfOverZ s B hS hZ)⟩ :
          AlgebraicSpaces B s.S hS) ⟶
        (⟨yoneda.obj (fppfOverX s B hS hX),
          isAlgebraicSpace_yoneda B s.S hS (fppfOverX s B hS hX)⟩ :
          AlgebraicSpaces B s.S hS))
      (ObjectProperty.homMk (yoneda.map (fppfOverJ s B hS hY hZ)) :
        (⟨yoneda.obj (fppfOverZ s B hS hZ),
          isAlgebraicSpace_yoneda B s.S hS (fppfOverZ s B hS hZ)⟩ :
          AlgebraicSpaces B s.S hS) ⟶
        (⟨yoneda.obj (fppfOverY s B hS hY),
          isAlgebraicSpace_yoneda B s.S hS (fppfOverY s B hS hY)⟩ :
          AlgebraicSpaces B s.S hS))
      (ObjectProperty.homMk (yoneda.map (fppfOverInl s B hS hX hP)) :
        (⟨yoneda.obj (fppfOverX s B hS hX),
          isAlgebraicSpace_yoneda B s.S hS (fppfOverX s B hS hX)⟩ :
          AlgebraicSpaces B s.S hS) ⟶
        (⟨yoneda.obj (fppfOverPushout s B hS hP),
          isAlgebraicSpace_yoneda B s.S hS (fppfOverPushout s B hS hP)⟩ :
          AlgebraicSpaces B s.S hS))
      (ObjectProperty.homMk (yoneda.map (fppfOverInr s B hS hY hP)) :
        (⟨yoneda.obj (fppfOverY s B hS hY),
          isAlgebraicSpace_yoneda B s.S hS (fppfOverY s B hS hY)⟩ :
          AlgebraicSpaces B s.S hS) ⟶
        (⟨yoneda.obj (fppfOverPushout s B hS hP),
          isAlgebraicSpace_yoneda B s.S hS (fppfOverPushout s B hS hP)⟩ :
          AlgebraicSpaces B s.S hS))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 81.7, Tag 0GG2](https://stacks.math.columbia.edu/tag/0GG2)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
