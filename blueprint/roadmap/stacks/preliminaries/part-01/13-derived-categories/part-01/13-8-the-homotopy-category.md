---
declaration: section
origin: cited
lean: CochainComplex.minus, CochainComplex.Minus, CochainComplex.bounded, CochainComplex.Bounded, HomotopyCategory.minus, HomotopyCategory.Minus, HomotopyCategory.bounded, HomotopyCategory.Bounded
statement: formalized
proof: formalized
---

# 13.8 The homotopy category

Section 13.8 of the Stacks Project, [Tag 05RN](https://stacks.math.columbia.edu/tag/05RN). 1 tag here is carried by 8 declarations of the repository (all in StacksFrontier) and 6 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 013H, a definition

[Tag 013H](https://stacks.math.columbia.edu/tag/013H) in the Stacks Project.

**`CochainComplex.minus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/HomotopyCategory/Minus.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/HomotopyCategory/Minus.lean#L50). The attribute's comment: “(3) bounded above complexes”. References: EGA 0 (11.2.1), “bounded above”; SGA 4½ Etat 0 (1.2.3), “bounded-above complexes”.

> The property of cochain complexes that are bounded above.

```lean
public def minus : ObjectProperty (CochainComplex C ℤ)
```

**`CochainComplex.Minus`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/HomotopyCategory/Minus.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/HomotopyCategory/Minus.lean#L62). The attribute's comment: “(5) Comp⁻(A), the full subcategory of bounded above complexes”.

> `Comp⁻(C)`: the full subcategory of `CochainComplex C ℤ` consisting of the bounded above
> complexes.

```lean
abbrev Minus
```

**`CochainComplex.bounded`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean#L130). The attribute's comment: “(4) bounded complexes”.

> The property of bounded cochain complexes.

```lean
def bounded (C : Type*) [Category* C] [Preadditive C] : ObjectProperty (CochainComplex C ℤ)
```

**`CochainComplex.Bounded`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean#L143). The attribute's comment: “(5) Compᵇ(A), the full subcategory of bounded complexes”.

> `Compᵇ(C)`: the full subcategory of `CochainComplex C ℤ` consisting of the bounded
> complexes.

```lean
abbrev Bounded (C : Type*) [Category* C] [Preadditive C]
```

**`HomotopyCategory.minus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean#L189). The attribute's comment: “(7) K⁻(A), as a property of objects of K(A)”. References: SGA 4 XVII (2.2.10), “partial”.

> The property of objects in the homotopy category represented by bounded-above
> cochain complexes.

```lean
def minus : ObjectProperty (HomotopyCategory C (.up ℤ))
```

**`HomotopyCategory.Minus`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean, line 235](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean#L235). The attribute's comment: “(7) K⁻(A)”. References: SGA 4 XVII (2.2.10), “special case”.

> The homotopy category of bounded-above cochain complexes.

```lean
abbrev Minus
```

**`HomotopyCategory.bounded`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean, line 247](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean#L247). The attribute's comment: “(7) Kᵇ(A), as a property of objects of K(A)”. References: SGA 4 XVII (2.2.10), “partial”.

> The property of objects in the homotopy category represented by bounded
> cochain complexes.

```lean
def bounded : ObjectProperty (HomotopyCategory C (.up ℤ))
```

**`HomotopyCategory.Bounded`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean, line 295](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean#L295). The attribute's comment: “(7) Kᵇ(A)”. References: SGA 4 XVII (2.2.10), “special case”.

> The homotopy category of bounded cochain complexes.

```lean
abbrev Bounded
```

Declarations registered for the tag:

- [`CochainComplex`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean, line 1576](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean#L1576) (StacksFrontier): “(1) Comp(A), the category of cochain complexes”. References: EGA 0 (11.2.1); EGA 0 (13.2.3); EGA III (6.2.1); SGA 2 VIII (1.2); SGA 4 XVII (2.2.7), “special case”; SGA 4 XVII (5.5.3); SGA 4½ Etat 0 (1.2.1); SGA 6 I (1.1.5).
- [`CochainComplex.plus`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex.plus#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean, line 1578](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean#L1578) (StacksFrontier): “(2) bounded below complexes”. References: EGA 0 (11.2.1), “special case”; SGA 2 VIII (1.4); SGA 4½ Etat 0 (1.2.3).
- [`CochainComplex.Plus`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex.Plus#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean, line 1580](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean#L1580) (StacksFrontier): “(5) Comp⁺(A), the full subcategory of bounded below complexes”. References: SGA 2 VIII (1.4); SGA 4 Vbis (2.5.1), “partial”.
- [`HomotopyCategory`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomotopyCategory#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean, line 1583](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean#L1583) (StacksFrontier): “(6) K(A), with homotopy classes of maps as morphisms (at `ComplexShape.up ℤ`)”. References: EGA 0 (20.6.26); SGA 4 Vbis (2.5.1); SGA 4 XVII (2.2.8), “absolute case of K(A/B)”; SGA 4½ Etat 0 (1.2.2); SGA 4½ Rapport (4.3), “arrows of K\_parf(Λ)”; SGA 6 I (1.1.5), “partial”.
- [`HomotopyCategory.plus`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomotopyCategory.plus#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean, line 1586](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean#L1586) (StacksFrontier): “(7) K⁺(A), as a property of objects of K(A)”. References: SGA 4 Vbis (2.3.3), “(A)”; SGA 4 Vbis (2.5.1), “partial”; SGA 4 XVII (2.2.10), “partial”; SGA 4½ Etat 0 (1.2.3).
- [`HomotopyCategory.Plus`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomotopyCategory.Plus#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean, line 1588](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/HomotopyCategory/Triangulated.lean#L1588) (StacksFrontier): “(7) K⁺(A)”. References: SGA 4 Vbis (2.3.3), “(A)”; SGA 4 Vbis (2.5.1), “K⁺(F(A))”; SGA 4 XVII (2.2.10), “special case”; SGA 4½ Etat 0 (1.2.3); SGA 6 I (1.1.5), “the fiber K⁺(C\_X)”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.8, Tag 05RN](https://stacks.math.columbia.edu/tag/05RN)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
