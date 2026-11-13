---
declaration: section
origin: cited
lean: DifferentialGradedModule.mem_distinguishedConeTriangles_iff_isDistinguishedTriangle_signTwist_mapTriangle, DifferentialGradedModule.exists_pretriangulated_structure, DifferentialGradedModule.octahedron_of_admissible_monos, DifferentialGradedModule.octahedron_of_isAdmissibleMono, DifferentialGradedModule.instIsTriangulatedHomotopyCategory', DifferentialGradedModule.instIsTriangulatedHomotopyCategory
statement: formalized
proof: formalized
---

# 22.10 The homotopy category is triangulated

Section 22.10 of the Stacks Project, [Tag 09KG](https://stacks.math.columbia.edu/tag/09KG). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09KH, a lemma

[Tag 09KH](https://stacks.math.columbia.edu/tag/09KH) in the Stacks Project.

**`DifferentialGradedModule.mem_distinguishedConeTriangles_iff_isDistinguishedTriangle_signTwist_mapTriangle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/ConeSignTransfer.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/ConeSignTransfer.lean#L149). The attribute's comment: “the cone-triangle structure against the admissible-sequence structure: the two are exchanged by the sign-twisted identity of the homotopy category”.

> **The two pretriangulated structures on `K(Mod_(A, d))` are exchanged by the sign-twisted
> identity.** A triangle lies in the cone class exactly when its image under `signTwist A` is the
> triangle of an admissible short exact sequence, and symmetrically. The two structures are
> therefore equivalent as pretriangulated categories, by an equivalence which is the identity on
> objects and on morphisms and twists only the comparison with the shift; they are *not* the same
> structure, the two classes of triangles being the two sign conventions for the third arrow.

```lean
theorem mem_distinguishedConeTriangles_iff_isDistinguishedTriangle_signTwist_mapTriangle
    (T : Triangle (HomotopyCategory.{u, v, w} A)) :
    T ∈ distinguishedConeTriangles.{u, v, w} (A := A) ↔
      IsDistinguishedTriangle A ((signTwist.{u, v, w} A).mapTriangle.obj T)
```

**`DifferentialGradedModule.exists_pretriangulated_structure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/Pretriangulated.lean, line 562](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/Pretriangulated.lean#L562).

> There is a pretriangulated structure on the homotopy category of differential
> graded modules whose distinguished triangles are precisely those arising from
> admissible short exact sequences.

```lean
theorem exists_pretriangulated_structure :
    ∃ p : Pretriangulated (HomotopyCategory A),
      p.distinguishedTriangles = {T | IsDistinguishedTriangle A T}
```

## Tag 09KI, a lemma

[Tag 09KI](https://stacks.math.columbia.edu/tag/09KI) in the Stacks Project.

**`DifferentialGradedModule.octahedron_of_admissible_monos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/Octahedron.lean, line 379](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/Octahedron.lean#L379).

> **Tag 09KI.** Two composable admissible monomorphisms of differential graded modules have
> distinguished triangles completing them to an octahedron: there are distinguished triangles
> `(K, L, Q₁)`, `(K, M, Q₂)` and `(L, M, Q₃)` on `α`, on `β ∘ α` and on `β`, together with maps
> `a : Q₁ ⟶ Q₂` and `b : Q₂ ⟶ Q₃` satisfying the four commutations of (TR 4), for which the
> triangle `(Q₁, Q₂, Q₃)` is itself distinguished.

```lean
theorem octahedron_of_admissible_monos (α : K ⟶ L) (β : L ⟶ M)
    (_hα : IsAdmissibleMono α) (_hβ : IsAdmissibleMono β) :
    letI q := toHomotopyCategory A
    ∃ (Q₁ Q₂ Q₃ : HomotopyCategory.{u, v, w} A)
      (p₁ : q.obj L ⟶ Q₁) (d₁ : Q₁ ⟶ (q.obj K)⟦(1 : ℤ)⟧)
      (p₂ : q.obj M ⟶ Q₂) (d₂ : Q₂ ⟶ (q.obj K)⟦(1 : ℤ)⟧)
      (p₃ : q.obj M ⟶ Q₃) (d₃ : Q₃ ⟶ (q.obj L)⟦(1 : ℤ)⟧)
      (a : Q₁ ⟶ Q₂) (b : Q₂ ⟶ Q₃),
      Triangle.mk (q.map α) p₁ d₁ ∈ distTriang (HomotopyCategory.{u, v, w} A) ∧
      Triangle.mk (q.map α ≫ q.map β) p₂ d₂ ∈ distTriang (HomotopyCategory.{u, v, w} A) ∧
      Triangle.mk (q.map β) p₃ d₃ ∈ distTriang (HomotopyCategory.{u, v, w} A) ∧
      (p₁ ≫ a = q.map β ≫ p₂) ∧
      (a ≫ d₂ = d₁) ∧
      (p₂ ≫ b = p₃) ∧
      (d₂ ≫ (q.map α)⟦(1 : ℤ)⟧' = b ≫ d₃) ∧
      Triangle.mk a b (d₃ ≫ p₁⟦(1 : ℤ)⟧') ∈ distTriang (HomotopyCategory.{u, v, w} A)
```

**`DifferentialGradedModule.octahedron_of_isAdmissibleMono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/DerivedCategory/Octahedron.lean, line 398](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/DerivedCategory/Octahedron.lean#L398).

> Two composable homomorphisms of differential graded modules have distinguished triangles
> forming an octahedron.

```lean
theorem octahedron_of_isAdmissibleMono {K L M : DifferentialGradedModule A}
    (α : Hom K L) (β : Hom L M) (_hα : IsAdmissibleMono α) (_hβ : IsAdmissibleMono β) :
    let q := toHomotopyCategory A
    ∃ (Q₁ Q₂ Q₃ : HomotopyCategory A)
      (p₁ : q.obj L ⟶ Q₁) (d₁ : Q₁ ⟶ (q.obj K)⟦(1 : ℤ)⟧)
      (p₂ : q.obj M ⟶ Q₂) (d₂ : Q₂ ⟶ (q.obj K)⟦(1 : ℤ)⟧)
      (p₃ : q.obj M ⟶ Q₃) (d₃ : Q₃ ⟶ (q.obj L)⟦(1 : ℤ)⟧)
      (a : Q₁ ⟶ Q₂) (b : Q₂ ⟶ Q₃),
      IsDistinguishedTriangle A (Pretriangulated.Triangle.mk (q.map α) p₁ d₁) ∧
      IsDistinguishedTriangle A
        (Pretriangulated.Triangle.mk (q.map α ≫ q.map β) p₂ d₂) ∧
      IsDistinguishedTriangle A (Pretriangulated.Triangle.mk (q.map β) p₃ d₃) ∧
      (p₁ ≫ a = q.map β ≫ p₂) ∧
      (a ≫ d₂ = d₁) ∧
      (p₂ ≫ b = p₃) ∧
      (d₂ ≫ (q.map α)⟦1⟧' = b ≫ d₃) ∧
      IsDistinguishedTriangle A
        (Pretriangulated.Triangle.mk a b (d₃ ≫ p₁⟦1⟧'))
```

## Tag 09KJ, a proposition

[Tag 09KJ](https://stacks.math.columbia.edu/tag/09KJ) in the Stacks Project.

**`DifferentialGradedModule.instIsTriangulatedHomotopyCategory'`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/Triangulated.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/Triangulated.lean#L71). References: SGA 4½ Etat 0 (1.2.2), “special case”.

> The homotopy category of differential graded modules is triangulated: the pretriangulated
> structure of Tag 09KH satisfies the octahedron axiom.
>
> Stated against `DifferentialGradedModule.instPretriangulatedHomotopyCategory'`, whose
> distinguished triangles are those of an admissible short exact sequence. The homonymous
> instance in `StacksFrontier/Algebra/DGA/Octahedron.lean` is the same axiom for the *other*
> pretriangulated structure, `DifferentialGradedModule.instPretriangulatedHomotopyCategory`,
> whose distinguished triangles are the cone triangles; the two are distinct statements and
> carry distinct names.

```lean
instance instIsTriangulatedHomotopyCategory' (A : DifferentialGradedAlgebra.{u, v} R) :
    IsTriangulated (HomotopyCategory.{u, v, w} A)
```

Declarations registered for the tag:

- [`DifferentialGradedModule.instIsTriangulatedHomotopyCategory`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/Octahedron.lean#L405), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Algebra/DifferentialGraded/DerivedCategory/Triangulated.lean, line 27](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/DerivedCategory/Triangulated.lean#L27) (StacksFrontier): “the homotopy category is triangulated”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 22.10, Tag 09KG](https://stacks.math.columbia.edu/tag/09KG)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
