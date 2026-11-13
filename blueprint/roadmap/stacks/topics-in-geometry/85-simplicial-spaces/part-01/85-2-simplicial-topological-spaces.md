---
declaration: section
origin: cited
lean: Stacks.Topology.Simplicial.ConstantSpace.systemCosimplicialEquivalence, Stacks.Topology.Simplicial.ConstantSpace.sheafCosimplicialEquivalence, Stacks.Topology.Simplicial.cechNerveTerminalFrom_δ_π, Stacks.Topology.Simplicial.cechNerveTerminalFrom_σ_π, Stacks.Topology.Simplicial.SimplicialOpen.toTopCat, Stacks.Topology.Simplicial.SimplicialOpen.toTopCat_map_comp_inclusion, Stacks.Topology.Simplicial.componentPresheaf_isSheaf, Stacks.Topology.Simplicial.SimplicialSheafSystem.transitionMap_comp
statement: formalized
proof: formalized
---

# 85.2 Simplicial topological spaces

Section 85.2 of the Stacks Project, [Tag 09VK](https://stacks.math.columbia.edu/tag/09VK). 13 tags here are carried by 60 declarations of the repository (all in StacksFrontier) and 30 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09VK, the section

[Tag 09VK](https://stacks.math.columbia.edu/tag/09VK) in the Stacks Project.

**`Stacks.Topology.Simplicial.ConstantSpace.systemCosimplicialEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/ConstantSpaceSheaves.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/ConstantSpaceSheaves.lean#L126). The attribute's comment: “systems `(F_n, F(φ))` on the constant simplicial space `X_•` are cosimplicial objects in the category of sheaves on `X`”.

> **A system of sheaves on the constant simplicial space on `X` is the same thing as a
> cosimplicial sheaf on `X`.**

```lean
def systemCosimplicialEquivalence :
    SimplicialSheafSystem (constantSpace X) A ≌ CosimplicialObject (TopCat.Sheaf A X)
```

**`Stacks.Topology.Simplicial.ConstantSpace.sheafCosimplicialEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/ConstantSpaceSheaves.lean, line 151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/ConstantSpaceSheaves.lean#L151). The attribute's comment: “by Lemma 09VM a sheaf on `X_{•,Zar}` is the same thing as a cosimplicial object in the category of sheaves on `X`”.

> **A sheaf on `X_{•,Zar}` is the same thing as a cosimplicial object in the category of
> sheaves on `X`.** The equivalence is the description of Lemma 09VM
> (`Stacks.Topology.Simplicial.sheafEquivalenceSimplicialSheafSystem`) followed by
> `systemCosimplicialEquivalence`; the sheaf in degree `[n]` of the cosimplicial object attached to
> a sheaf `F` is the restriction `F_n` of `F` to the opens of the `n`-th copy of `X`.

```lean
def sheafCosimplicialEquivalence :
    Sheaf (SimplicialOpen.grothendieckTopology (constantSpace X)) A ≌
      CosimplicialObject (TopCat.Sheaf A X)
```

**`Stacks.Topology.Simplicial.cechNerveTerminalFrom_δ_π`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/SimplicialSpace.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/SimplicialSpace.lean#L119). The attribute's comment: “the face map `d^n_i` is the projection forgetting the `i`-th coordinate”.

> **The face map `d^{n+1}_i` forgets the `i`-th coordinate.** On the simplicial object
> `X_n = Y^{n+1}`, the `k`-th coordinate of `d_i` is the `(i.succAbove k)`-th coordinate, i.e. the
> coordinates of `d_i(y_0, …, y_{n+1})` are those of `(y_0, …, y_{n+1})` with `y_i` left out.

```lean
theorem cechNerveTerminalFrom_δ_π {n : ℕ} (i : Fin (n + 2)) (k : Fin (n + 1)) :
    (cechNerveTerminalFrom Y).δ i ≫ Pi.π (fun _ : Fin (n + 1) => Y) k =
      Pi.π (fun _ : Fin (n + 2) => Y) (i.succAbove k)
```

**`Stacks.Topology.Simplicial.cechNerveTerminalFrom_σ_π`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/SimplicialSpace.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/SimplicialSpace.lean#L128). The attribute's comment: “the degeneracy map `s^n_j` is the diagonal repeating the `j`-th coordinate”.

> **The degeneracy map `s^n_j` repeats the `j`-th coordinate.** On the simplicial object
> `X_n = Y^{n+1}`, the `k`-th coordinate of `s_j` is the `(j.predAbove k)`-th coordinate, i.e.
> `s_j(y_0, …, y_n) = (y_0, …, y_j, y_j, …, y_n)`.

```lean
theorem cechNerveTerminalFrom_σ_π {n : ℕ} (j : Fin (n + 1)) (k : Fin (n + 2)) :
    (cechNerveTerminalFrom Y).σ j ≫ Pi.π (fun _ : Fin (n + 2) => Y) k =
      Pi.π (fun _ : Fin (n + 1) => Y) (j.predAbove k)
```

**`Stacks.Topology.Simplicial.SimplicialOpen.toTopCat`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/SimplicialSpace.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/SimplicialSpace.lean#L153). The attribute's comment: “a morphism `U → V` of `X_Zar` given by `φ` induces a continuous map `U → V`”.

> **A morphism of `X_Zar` induces a continuous map.** An object `U ⊆ X_n` of the site of a
> simplicial space is a topological space, and a morphism `U → V` given by `φ` induces the
> continuous map `U → V` restricting `X(φ) : X_n → X_m`.

```lean
def toTopCat : SimplicialOpen X ⥤ TopCat.{u}
```

**`Stacks.Topology.Simplicial.SimplicialOpen.toTopCat_map_comp_inclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/SimplicialSpace.lean, line 172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/SimplicialSpace.lean#L172). The attribute's comment: “the induced continuous map `U → V` is the restriction of `X(φ)`”.

> The continuous map `U → V` induced by a morphism given by `φ` is the restriction of
> `X(φ) : X_n → X_m`.

```lean
theorem toTopCat_map_comp_inclusion {U V : SimplicialOpen X} (f : U ⟶ V) :
    (toTopCat X).map f ≫ V.toOpens.inclusion' = U.toOpens.inclusion' ≫ X.map f.base
```

**`Stacks.Topology.Simplicial.componentPresheaf_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/SimplicialSpace.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/SimplicialSpace.lean#L204). The attribute's comment: “the restriction `F_n` of a sheaf `F` on `X_Zar` to the opens of `X_n` is a sheaf”.

> **The restriction `F_n` of a sheaf on `X_Zar` to the opens of `X_n` is a sheaf on `X_n`.**
> This holds for sheaves with values in any category.

```lean
theorem componentPresheaf_isSheaf {X : SimplicialObject TopCat.{u}} {A : Type w} [Category.{v} A]
    (F : Sheaf (SimplicialOpen.grothendieckTopology X) A) (n : SimplexCategoryᵒᵖ) :
    TopCat.Presheaf.IsSheaf (componentPresheaf F.obj n)
```

**`Stacks.Topology.Simplicial.SimplicialSheafSystem.transitionMap_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/SimplicialSpace.lean, line 225](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/SimplicialSpace.lean#L225). The attribute's comment: “`F(φ) ∘ F(ψ) = F(φ ∘ ψ)`, composition of `f`-maps as in Sheaves 008L”.

> **`F(φ) ∘ F(ψ) = F(φ ∘ ψ)`.** The composite (Stacks 008L) of the `f`-maps `F(φ)` and `F(ψ)`
> is the `f`-map of the composite. It is an `(X(φ) ≫ X(ψ))`-map while `F(φ ≫ ψ)` is an
> `X(φ ≫ ψ)`-map, so the equality is heterogeneous.

```lean
theorem transitionMap_comp (P : (SimplicialOpen X)ᵒᵖ ⥤ A) {l m n : SimplexCategoryᵒᵖ}
    (φ : l ⟶ m) (ψ : m ⟶ n) :
    HEq ((transitionMap P φ).compPresheaf (transitionMap P ψ)) (transitionMap P (φ ≫ ψ))
```

**`Stacks.Topology.Simplicial.sheafSystem`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/SimplicialSpace.lean, line 255](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/SimplicialSpace.lean#L255). The attribute's comment: “a sheaf `F` on `X_Zar` gives the system `(F_n, F(φ))`”.

> **The system `(F_n, F(φ))` of a sheaf on `X_Zar`.** A sheaf `F` on the site of a simplicial
> space gives the sheaves `F_n` on the spaces `X_n`, obtained by restricting `F` to the opens of
> `X_n`, together with the `X(φ)`-maps `F(φ) : F_m → F_n` formed by the restriction maps of `F`,
> which satisfy `F(φ) ∘ F(ψ) = F(φ ∘ ψ)` and `F(id) = id`.

```lean
def sheafSystem :
    Sheaf (SimplicialOpen.grothendieckTopology X) A ⥤ SimplicialSheafSystem X A
```

**`Stacks.Topology.Simplicial.systemSheafCompSheafSystemIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/SimplicialSpace.lean, line 384](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/SimplicialSpace.lean#L384). The attribute's comment: “conversely, a system `(F_n, F(φ))` with `F(φ) ∘ F(ψ) = F(φ ∘ ψ)` and `F(id) = id` gives a sheaf on `X_Zar` whose system it is”.

> **A system is the system of its sheaf.** The sheaf on `X_Zar` defined by a system
> `(F_n, F(φ))` has, as its restrictions to the opens of the `X_n` and as its restriction maps along
> the morphisms given by the `φ`, the system `(F_n, F(φ))` again, naturally in the system.

```lean
def systemSheafCompSheafSystemIso : systemSheaf X A ⋙ sheafSystem X A ≅ 𝟭 _
```

Declarations registered for the tag:

- [`constantSpace`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=constantSpace#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Simplicial/ConstantSpaceSheaves.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/ConstantSpaceSheaves.lean#L48) (StacksFrontier): “the constant simplicial topological space `X_•` with value `X`”.
- [`CategoryTheory.SimplicialObject`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.SimplicialObject#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Simplicial/SimplicialSpace.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/SimplicialSpace.lean#L85) (StacksFrontier): “a simplicial space: a simplicial object of the category of topological spaces and continuous maps, `SimplicialObject TopCat`”. References: SGA 4 V (7.1.0); SGA 4 Vbis (1.2.6); SGA 4 Vbis (3.0.1); SGA 4 Vbis (5.1.0).
- [`CategoryTheory.SimplicialObject.δ`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.SimplicialObject.δ#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Simplicial/SimplicialSpace.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/SimplicialSpace.lean#L91) (StacksFrontier): “the face maps `d^n_i : X_n → X_{n-1}`; for `n = 1` the two maps `d^1_0, d^1_1`”. References: SGA 4 V (1.10); SGA 4 Vbis (5.1.0).
- [`CategoryTheory.SimplicialObject.σ`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.SimplicialObject.σ#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Simplicial/SimplicialSpace.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/SimplicialSpace.lean#L95) (StacksFrontier): “the degeneracy maps `s^n_j : X_n → X_{n+1}`; for `n = 0` the single `s^0_0`”. References: SGA 4 Vbis (5.1.0).
- [`CategoryTheory.SimplicialObject.δ_comp_σ_self`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.SimplicialObject.δ_comp_σ_self#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Simplicial/SimplicialSpace.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/SimplicialSpace.lean#L98) (StacksFrontier): “`d_j ∘ s_j = id`: the diagonal repeating the `j`-th coordinate followed by forgetting it”.
- [`CategoryTheory.SimplicialObject.δ_comp_σ_succ`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.SimplicialObject.δ_comp_σ_succ#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Simplicial/SimplicialSpace.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/SimplicialSpace.lean#L100) (StacksFrontier): “`d_{j+1} ∘ s_j = id`: the diagonal repeating the `j`-th coordinate followed by forgetting the repeated copy”.
- [`CategoryTheory.cechNerveTerminalFrom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.cechNerveTerminalFrom#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Simplicial/SimplicialSpace.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/SimplicialSpace.lean#L102) (StacksFrontier): “the model `X_n = Y^{n+1}` of the picture of a simplicial space”. References: SGA 3 X (6.3); SGA 3 X (9.7.1); SGA 4 V (1.10), “special case”; SGA 4 Vbis (1.2.7), “special case”.
- [`SimplicialOpen`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SimplicialOpen#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Simplicial/SimplicialSpace.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/SimplicialSpace.lean#L137) (StacksFrontier): “(1) an object of `X_Zar` is an open `U` of `X_n` for some `n`”.
- [`SimplicialOpen.Hom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SimplicialOpen.Hom#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Simplicial/SimplicialSpace.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/SimplicialSpace.lean#L138) (StacksFrontier): “(2) a morphism `U → V` of `X_Zar` is a `φ : [m] → [n]` with `X(φ)(U) ⊆ V`”.
- [`SimplicialOpen.IsCovering`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SimplicialOpen.IsCovering#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Simplicial/SimplicialSpace.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/SimplicialSpace.lean#L140) (StacksFrontier): “(3) a covering `{U_i → U}`: opens of one `X_n`, maps given by `id : [n] → [n]`, and `U = ⋃ U_i`”.
- [`SimplicialOpen.precoverage`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SimplicialOpen.precoverage#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Simplicial/SimplicialSpace.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/SimplicialSpace.lean#L142) (StacksFrontier): “the coverings of `X_Zar`”.
- [`SimplicialOpen.grothendieckTopology`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SimplicialOpen.grothendieckTopology#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Simplicial/SimplicialSpace.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/SimplicialSpace.lean#L143) (StacksFrontier): “the topology of `X_Zar`”.
- [`DiagramOpen`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DiagramOpen#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Simplicial/SimplicialSpace.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/SimplicialSpace.lean#L180) (StacksFrontier): “the site attached to an arbitrary diagram of topological spaces: its objects”.
- [`DiagramOpen.isoPrecoverage`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DiagramOpen.isoPrecoverage#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Simplicial/SimplicialSpace.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/SimplicialSpace.lean#L182) (StacksFrontier): “the site attached to an arbitrary diagram of topological spaces: its coverings”.
- [`DiagramOpen.isoPrecoverage_hasIsos`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DiagramOpen.isoPrecoverage_hasIsos#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Simplicial/SimplicialSpace.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/SimplicialSpace.lean#L184) (StacksFrontier): “the site attached to an arbitrary diagram of topological spaces: the identity-covering axiom”.
- [`DiagramOpen.isoPrecoverage_hasPullbacks`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DiagramOpen.isoPrecoverage_hasPullbacks#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Simplicial/SimplicialSpace.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/SimplicialSpace.lean#L186) (StacksFrontier): “the site attached to an arbitrary diagram of topological spaces: existence of pullbacks of coverings”.
- [`DiagramOpen.isoPrecoverage_isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DiagramOpen.isoPrecoverage_isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Simplicial/SimplicialSpace.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/SimplicialSpace.lean#L188) (StacksFrontier): “the site attached to an arbitrary diagram of topological spaces: the base-change axiom”.
- [`DiagramOpen.isoPrecoverage_isStableUnderComposition`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DiagramOpen.isoPrecoverage_isStableUnderComposition#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Simplicial/SimplicialSpace.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/SimplicialSpace.lean#L190) (StacksFrontier): “the site attached to an arbitrary diagram of topological spaces: the composition axiom”.
- [`DiagramOpen.isoPrecoverage_eq_precoverage`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DiagramOpen.isoPrecoverage_eq_precoverage#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Simplicial/SimplicialSpace.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/SimplicialSpace.lean#L192) (StacksFrontier): “for a simplicial space its coverings are the levelwise open coverings”.
- [`simplicialOpenEquiv`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=simplicialOpenEquiv#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Simplicial/SimplicialSpace.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/SimplicialSpace.lean#L194) (StacksFrontier): “`X_Zar` is the site of the diagram `X` of spaces: the identification of categories”.
- [`toDiagramOpen_isDenseSubsite`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=toDiagramOpen_isDenseSubsite#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Simplicial/SimplicialSpace.lean, line 196](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/SimplicialSpace.lean#L196) (StacksFrontier): “`X_Zar` is the site of the diagram `X` of spaces: the identification is one of sites”.
- [`componentPresheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=componentPresheaf#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Simplicial/SimplicialSpace.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/SimplicialSpace.lean#L210) (StacksFrontier): “the restriction `F_n` of a presheaf on `X_Zar` to the opens of `X_n`”.
- [`SimplicialSheafSystem.transitionMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SimplicialSheafSystem.transitionMap#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Simplicial/SimplicialSpace.lean, line 212](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/SimplicialSpace.lean#L212) (StacksFrontier): “the restriction maps of `F` for `X(φ)(U) ⊆ V` define an `X(φ)`-map `F(φ) : F_m → F_n`”.
- [`transitionMap_id_app`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=transitionMap_id_app#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Simplicial/SimplicialSpace.lean, line 219](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/SimplicialSpace.lean#L219) (StacksFrontier): “`F(id_{[n]}) = id_{F_n}`”.
- [`SimplicialSheafSystem`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SimplicialSheafSystem#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Simplicial/SimplicialSpace.lean, line 243](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/SimplicialSpace.lean#L243) (StacksFrontier): “a system `({F_n}, {F(φ)})`: sheaves on the `X_n` with `X(φ)`-maps satisfying `F(φ) ∘ F(ψ) = F(φ ∘ ψ)` and `F(id) = id`”.
- [`_root_.Opens.pretopology`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=_root_.Opens.pretopology#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Simplicial/SimplicialSpace.lean, line 392](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/SimplicialSpace.lean#L392) (StacksFrontier): “for a topological space `X`, the site `X_Zar` of opens of `X` with inclusions and open coverings (Sites, Example 00VJ)”.
- [`_root_.Opens.pretopology_toGrothendieck`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=_root_.Opens.pretopology_toGrothendieck#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Simplicial/SimplicialSpace.lean, line 396](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/SimplicialSpace.lean#L396) (StacksFrontier): “the topos `Sh(X_Zar)` is identified with the category of sheaves on `X`: the topology generated by the open coverings is the topology of sheaves on `X`”.
- [`TopCat.Sheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.Sheaf#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Simplicial/SimplicialSpace.lean, line 399](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/SimplicialSpace.lean#L399) (StacksFrontier): “the category of sheaves on a topological space `X`, that is, `Sh(X_Zar)`”. References: EGA 0 (3.1.4); EGA 0 (3.1.2); SGA 3 IV (4.3.1), “special case”; SGA 3 IV (4.3.18), “special case”; SGA 4 II (6.1), “special case”; SGA 4 IV (0.1), “special case”; SGA 4 IV (2.1); SGA 4 VI (1.22.1); SGA 4 Vbis (4.2.0), “Fiber of E over a scheme”; SGA 4½ Arcata (1.2.3), “more general”; SGA 4½ Arcata (1.6.3), “topological site”; SGA 4 II (2.1), “opens of a space”.

## Tag 09VL, a lemma

[Tag 09VL](https://stacks.math.columbia.edu/tag/09VL) in the Stacks Project.

**`Stacks.Topology.Simplicial.SimplicialOpen.precoverage_hasIsos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/Site.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/Site.lean#L149). The attribute's comment: “the identity-covering axiom”.

> **Stacks 09VL.** Singleton isomorphisms are levelwise open covering families.

```lean
theorem precoverage_hasIsos (X : SimplicialObject TopCat.{u}) :
    (precoverage X).HasIsos
```

**`Stacks.Topology.Simplicial.SimplicialOpen.precoverage_hasPullbacks`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/Site.lean, line 217](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/Site.lean#L217). The attribute's comment: “existence of pullbacks of coverings”.

> **Stacks 09VL.** Pullbacks of arrows in a levelwise open covering family along arbitrary
> morphisms exist.

```lean
theorem precoverage_hasPullbacks (X : SimplicialObject TopCat.{u}) :
    (precoverage X).HasPullbacks
```

**`Stacks.Topology.Simplicial.SimplicialOpen.precoverage_isStableUnderBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/Site.lean, line 274](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/Site.lean#L274). The attribute's comment: “the base-change axiom”.

> **Stacks 09VL.** Levelwise open covering families are stable under base change.

```lean
theorem precoverage_isStableUnderBaseChange (X : SimplicialObject TopCat.{u}) :
    (precoverage X).IsStableUnderBaseChange
```

**`Stacks.Topology.Simplicial.SimplicialOpen.precoverage_isStableUnderComposition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/Site.lean, line 310](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/Site.lean#L310). The attribute's comment: “the composition axiom”.

> **Stacks 09VL.** Levelwise open covering families are stable under composition.

```lean
theorem precoverage_isStableUnderComposition (X : SimplicialObject TopCat.{u}) :
    (precoverage X).IsStableUnderComposition
```

## Tag 09VM, a lemma

[Tag 09VM](https://stacks.math.columbia.edu/tag/09VM) in the Stacks Project.

**`Stacks.Topology.Simplicial.isEquivalence_sheafToSimplicialSheafSystem`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/Sheaves.lean, line 869](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/Sheaves.lean#L869).

> **Stacks 09VM.** Let `X` be a simplicial topological space. The functor
> `sheafToSimplicialSheafSystem` from sheaves on the site `X_Zar` of `X`
> (`SimplicialOpen.grothendieckTopology X`: opens of the spaces `X n`, morphisms over simplex
> maps, coverings by open coverings inside one degree) to the category `SimplicialSheafSystem X A`
> of systems `(F_n, F(φ))` of sheaves `F_n` on `X n` with `X.map φ`-maps `F(φ)` satisfying
> `F(φ) ∘ F(ψ) = F(φ ∘ ψ)` and `F(id) = id`, which sends `F` to its restrictions to the degrees
> and its restriction maps over simplex maps, is an equivalence of categories. The values are in
> an arbitrary category `A`; sheaves of sets are the case `A = Type _`.

```lean
instance isEquivalence_sheafToSimplicialSheafSystem
    (X : SimplicialObject TopCat.{u}) (A : Type w) [Category.{v} A] :
    (sheafToSimplicialSheafSystem (X := X) (A := A)).IsEquivalence
```

## Tag 09VN, a lemma

[Tag 09VN](https://stacks.math.columbia.edu/tag/09VN) in the Stacks Project.

**`Stacks.Topology.Simplicial.SimplicialOpen.pullback_isMorphismOfSites`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/Morphisms.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/Morphisms.lean#L200).

> **Stacks 09VN.** The simplicial-site morphism on sheaves in the universe of the spaces.

```lean
theorem pullback_isMorphismOfSites {X Y : SimplicialObject TopCat.{u}} (f : Y ⟶ X) :
    IsMorphismOfSites.{u} (pullback f)
      (SimplicialOpen.grothendieckTopology X)
      (SimplicialOpen.grothendieckTopology Y)
```

## Tag 09VP, a lemma

[Tag 09VP](https://stacks.math.columbia.edu/tag/09VP) in the Stacks Project.

**`AlgebraicGeometry.SimplicialScheme.componentModulePushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ZariskiPushforwardQuasicoherent.lean, line 151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ZariskiPushforwardQuasicoherent.lean#L151). The attribute's comment: “part (1) for sheaves of modules on the total Zariski site of a simplicial scheme”.

> **Stacks 09VP, part (1), for sheaves of modules on the total Zariski site.** The degree-`n`
> component of the pushforward of a sheaf of `𝒪_V`-modules along a morphism `f : V ⟶ U` of
> simplicial schemes is the pushforward of its degree-`n` component along `f_n : V_n ⟶ U_n`.

```lean
public noncomputable def componentModulePushforwardIso (f : V ⟶ U) (G : Modules V)
    (n : SimplexCategoryᵒᵖ) :
    (componentModule U n).obj ((modulePushforward f).obj G) ≅
      (Scheme.Modules.pushforward (f.app n)).obj ((componentModule V n).obj G)
```

**`Stacks.Topology.Simplicial.pushforwardComponentIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/ComponentFunctoriality.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/ComponentFunctoriality.lean#L58). The attribute's comment: “part (1)”.

> **Stacks 09VP, part (1).** The component in degree `n` of direct image along a
> morphism of simplicial spaces is the direct image along its degree-`n` component.

```lean
noncomputable def pushforwardComponentIso
    {X Y : SimplicialObject TopCat.{u}} (f : Y ⟶ X) (n : SimplexCategoryᵒᵖ) :
    letI : IsMorphismOfSites.{u} (SimplicialOpen.pullback f)
      (SimplicialOpen.grothendieckTopology X)
      (SimplicialOpen.grothendieckTopology Y) :=
        SimplicialOpen.pullback_isMorphismOfSites f
    (SimplicialOpen.pullback f).sheafPushforwardContinuous
        (Type u) (SimplicialOpen.grothendieckTopology X)
        (SimplicialOpen.grothendieckTopology Y) ⋙
      (sheafEquivalenceSimplicialSheafSystem X (Type u)).toEquivalence.functor ⋙
      SimplicialSheafSystem.componentFunctor X (Type u) n ≅
    (sheafEquivalenceSimplicialSheafSystem Y (Type u)).toEquivalence.functor ⋙
      SimplicialSheafSystem.componentFunctor Y (Type u) n ⋙
        TopCat.Sheaf.pushforward (Type u) (f.app n)
```

**`Stacks.Topology.Simplicial.pullbackComponentIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/ComponentFunctoriality.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/ComponentFunctoriality.lean#L158). The attribute's comment: “part (2)”.

> **Stacks 09VP, part (2).** The component in degree `n` of inverse image along a
> morphism of simplicial spaces is the inverse image along its degree-`n` component.

```lean
noncomputable def pullbackComponentIso
    {X Y : SimplicialObject TopCat.{u}} (f : Y ⟶ X) (n : SimplexCategoryᵒᵖ) :
    letI : IsMorphismOfSites.{u} (SimplicialOpen.pullback f)
      (SimplicialOpen.grothendieckTopology X)
      (SimplicialOpen.grothendieckTopology Y) :=
        SimplicialOpen.pullback_isMorphismOfSites f
    (SimplicialOpen.pullback f).sheafPullback
        (Type u) (SimplicialOpen.grothendieckTopology X)
        (SimplicialOpen.grothendieckTopology Y) ⋙
      (sheafEquivalenceSimplicialSheafSystem Y (Type u)).toEquivalence.functor ⋙
      SimplicialSheafSystem.componentFunctor Y (Type u) n ≅
    (sheafEquivalenceSimplicialSheafSystem X (Type u)).toEquivalence.functor ⋙
      SimplicialSheafSystem.componentFunctor X (Type u) n ⋙
      TopCat.Sheaf.pullback (Type u) (f.app n)
```

## Tag 09W0, a lemma

[Tag 09W0](https://stacks.math.columbia.edu/tag/09W0) in the Stacks Project.

**`Stacks.Topology.Simplicial.levelFunctor_isContinuous_mk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/ComponentSite.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/ComponentSite.lean#L53). The attribute's comment: “component\_site\_inclusion”.

> **Stacks 09W0.** The inclusion of the open-set site of one component into the site of
> simplicial opens is continuous.

```lean
theorem levelFunctor_isContinuous_mk (X : SimplicialObject TopCat.{u}) (n : ℕ) :
    (levelFunctor X (op (SimplexCategory.mk n))).IsContinuous
      (Opens.grothendieckTopology (X.obj (op (SimplexCategory.mk n))))
      (SimplicialOpen.grothendieckTopology X)
```

**`Stacks.Topology.Simplicial.levelFunctor_isCocontinuous_mk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/ComponentSite.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/ComponentSite.lean#L62). The attribute's comment: “component\_site\_inclusion”.

> **Stacks 09W0.** The inclusion of the open-set site of one component into the site of
> simplicial opens is cocontinuous.

```lean
theorem levelFunctor_isCocontinuous_mk (X : SimplicialObject TopCat.{u}) (n : ℕ) :
    (levelFunctor X (op (SimplexCategory.mk n))).IsCocontinuous
      (Opens.grothendieckTopology (X.obj (op (SimplexCategory.mk n))))
      (SimplicialOpen.grothendieckTopology X)
```

**`Stacks.Topology.Simplicial.inverseImageIsoComponent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/ComponentSite.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/ComponentSite.lean#L71). The attribute's comment: “inverse\_image\_is\_restriction”.

> **Stacks 09W0.** Pulling a sheaf back to a simplicial component is, naturally in that
> sheaf, its component in the sheaf-system description.

```lean
noncomputable def inverseImageIsoComponent
    (X : SimplicialObject TopCat.{u}) (n : ℕ) :
    (levelFunctor X (op (SimplexCategory.mk n))).sheafPullbackCocontinuous
        (Type u) (Opens.grothendieckTopology (X.obj (op (SimplexCategory.mk n))))
        (SimplicialOpen.grothendieckTopology X) ≅
      (sheafEquivalenceSimplicialSheafSystem X (Type u)).toEquivalence.functor ⋙
        SimplicialSheafSystem.componentFunctor X (Type u)
          (op (SimplexCategory.mk n))
```

**`Stacks.Topology.Simplicial.componentLowerShriek`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/LowerShriek.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/LowerShriek.lean#L82). The attribute's comment: “sheaf\_left\_adjoint”.

> The lower-shriek functor from sheaves of sets on one component to sheaves of sets on the
> simplicial site.

```lean
noncomputable def componentLowerShriek
    (X : SimplicialObject TopCat.{u}) (n : ℕ) :
    Sheaf (Opens.grothendieckTopology (X.obj (op (SimplexCategory.mk n)))) (Type u) ⥤
      Sheaf (SimplicialOpen.grothendieckTopology X) (Type u)
```

**`Stacks.Topology.Simplicial.componentLowerShriek_adjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/LowerShriek.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/LowerShriek.lean#L94). The attribute's comment: “sheaf\_left\_adjoint”.

> **Stacks 09W0.** Lower shriek is left adjoint to inverse image from the total
> simplicial site to a component.

```lean
noncomputable def componentLowerShriek_adjunction
    (X : SimplicialObject TopCat.{u}) (n : ℕ) :
    componentLowerShriek X n ⊣
      (levelFunctor X (op (SimplexCategory.mk n))).sheafPullbackCocontinuous
        (Type u) (Opens.grothendieckTopology (X.obj (op (SimplexCategory.mk n))))
        (SimplicialOpen.grothendieckTopology X)
```

**`Stacks.Topology.Simplicial.componentLowerShriek_preservesFiniteConnectedLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/LowerShriek.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/LowerShriek.lean#L106). The attribute's comment: “sheaf\_left\_adjoint\_connected\_limits”.

> **Stacks 09W0.** Lower shriek from a simplicial component preserves finite
> connected limits.

```lean
theorem componentLowerShriek_preservesFiniteConnectedLimits
    (X : SimplicialObject TopCat.{u}) (n : ℕ)
    (J : Type vC) [SmallCategory J] [FinCategory J] [IsConnected J] :
    PreservesLimitsOfShape J (componentLowerShriek X n)
```

**`Stacks.Topology.Simplicial.componentLowerShriekAb`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/LowerShriek.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/LowerShriek.lean#L120). The attribute's comment: “abelian\_left\_adjoint”.

> Lower shriek from sheaves of abelian groups on a component to sheaves of abelian groups on
> the total simplicial site.

```lean
noncomputable def componentLowerShriekAb
    (X : SimplicialObject TopCat.{u}) (n : ℕ) :
    Sheaf (Opens.grothendieckTopology (X.obj (op (SimplexCategory.mk n)))) Ab.{u} ⥤
      Sheaf (SimplicialOpen.grothendieckTopology X) Ab.{u}
```

**`Stacks.Topology.Simplicial.componentLowerShriekAb_adjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/LowerShriek.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/LowerShriek.lean#L134). The attribute's comment: “abelian\_left\_adjoint”.

> **Stacks 09W0.** Abelian lower shriek is left adjoint to restriction from
> the total simplicial site to a component.

```lean
noncomputable def componentLowerShriekAb_adjunction
    (X : SimplicialObject TopCat.{u}) (n : ℕ) :
    componentLowerShriekAb X n ⊣
      (levelFunctor X (op (SimplexCategory.mk n))).sheafPushforwardContinuous
        Ab.{u}
        (Opens.grothendieckTopology (X.obj (op (SimplexCategory.mk n))))
        (SimplicialOpen.grothendieckTopology X)
```

**`Stacks.Topology.Simplicial.componentLowerShriekAb_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/LowerShriek.lean, line 232](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/LowerShriek.lean#L232). The attribute's comment: “abelian\_left\_adjoint\_exact”.

> **Stacks 09W0.** Abelian lower shriek from a component of a simplicial space is exact.

```lean
theorem componentLowerShriekAb_exact
    (X : SimplicialObject TopCat.{u}) (n : ℕ)
    [∀ F : (Opens (X.obj (op (SimplexCategory.mk n))))ᵒᵖ ⥤ Ab.{w},
      (levelFunctor X (op (SimplexCategory.mk n))).op.HasLeftKanExtension F]
    [HasSheafify (SimplicialOpen.grothendieckTopology X) Ab.{w}] :
    exactFunctor
      (Sheaf (Opens.grothendieckTopology (X.obj (op (SimplexCategory.mk n)))) Ab.{w})
      (Sheaf (SimplicialOpen.grothendieckTopology X) Ab.{w})
      (Functor.sheafPullbackConstruction.sheafPullback
        (levelFunctor X (op (SimplexCategory.mk n))) Ab.{w}
        (Opens.grothendieckTopology (X.obj (op (SimplexCategory.mk n))))
        (SimplicialOpen.grothendieckTopology X))
```

**`Stacks.Topology.Simplicial.exactFunctor_componentLowerShriekAb`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/LowerShriek.lean, line 267](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/LowerShriek.lean#L267). The attribute's comment: “abelian\_left\_adjoint\_exact”.

> **Stacks 09W0**, part (5): `g_{n!}` is exact.  This is `componentLowerShriekAb_exact` for
> the registered functor `componentLowerShriekAb` and with no hypotheses: on the small site of
> opens of a topological space, with coefficients in abelian groups of the same universe, both
> the left Kan extensions and the sheafification used to build lower shriek exist.

```lean
theorem exactFunctor_componentLowerShriekAb (X : SimplicialObject TopCat.{u}) (n : ℕ) :
    exactFunctor
      (Sheaf (Opens.grothendieckTopology (X.obj (op (SimplexCategory.mk n)))) Ab.{u})
      (Sheaf (SimplicialOpen.grothendieckTopology X) Ab.{u})
      (componentLowerShriekAb X n)
```

## Tag 09W1, a lemma

[Tag 09W1](https://stacks.math.columbia.edu/tag/09W1) in the Stacks Project.

**`Stacks.Topology.Simplicial.componentRestrictionAb_preservesInjectiveObjects`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/LowerShriek.lean, line 280](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/LowerShriek.lean#L280). The attribute's comment: “restriction to a degree preserves injectives”.

> **Stacks 09W1.** Restriction of abelian sheaves from the site of a simplicial space to the
> site of one of its degrees preserves injective objects: it is right adjoint to lower shriek,
> which is exact.

```lean
theorem componentRestrictionAb_preservesInjectiveObjects
    (X : SimplicialObject TopCat.{u}) (n : ℕ)
    [∀ F : (Opens (X.obj (op (SimplexCategory.mk n))))ᵒᵖ ⥤ Ab.{w},
      (levelFunctor X (op (SimplexCategory.mk n))).op.HasLeftKanExtension F]
    [HasSheafify (SimplicialOpen.grothendieckTopology X) Ab.{w}]
    [HasSheafify (Opens.grothendieckTopology (X.obj (op (SimplexCategory.mk n)))) Ab.{w}] :
    ((levelFunctor X (op (SimplexCategory.mk n))).sheafPushforwardContinuous Ab.{w}
        (Opens.grothendieckTopology (X.obj (op (SimplexCategory.mk n))))
        (SimplicialOpen.grothendieckTopology X)).PreservesInjectiveObjects
```

**`Stacks.Topology.Simplicial.injective_component`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/LowerShriek.lean, line 337](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/LowerShriek.lean#L337).

> **Stacks 09W1.** If `I` is an injective abelian sheaf on the site of a simplicial space `X`,
> then its degree-`n` component `I n` is an injective abelian sheaf on `X n`.

```lean
theorem injective_component (X : SimplicialObject TopCat.{u}) (n : ℕ)
    [∀ F : (Opens (X.obj (op (SimplexCategory.mk n))))ᵒᵖ ⥤ Ab.{w},
      (levelFunctor X (op (SimplexCategory.mk n))).op.HasLeftKanExtension F]
    [HasSheafify (SimplicialOpen.grothendieckTopology X) Ab.{w}]
    [HasSheafify (Opens.grothendieckTopology (X.obj (op (SimplexCategory.mk n)))) Ab.{w}]
    (E : SheafSystemEquivalence X Ab.{w})
    (I : Sheaf (SimplicialOpen.grothendieckTopology X) Ab.{w}) [Injective I] :
    Injective ((E.toEquivalence.functor.obj I).component (op (SimplexCategory.mk n)))
```

## Tag 09W2, a lemma

[Tag 09W2](https://stacks.math.columbia.edu/tag/09W2) in the Stacks Project.

**`Stacks.Topology.Simplicial.componentPullbackNaturalityIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/ComponentFunctoriality.lean, line 302](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/ComponentFunctoriality.lean#L302).

> **Stacks 09W2.** Restriction to the `n`-th component commutes, naturally in the sheaf, with
> inverse image along a map of simplicial spaces.

```lean
noncomputable def componentPullbackNaturalityIso
    {X Y : SimplicialObject TopCat.{u}} (f : Y ⟶ X) (n : ℕ) :
    letI : IsMorphismOfSites.{u} (SimplicialOpen.pullback f)
      (SimplicialOpen.grothendieckTopology X)
      (SimplicialOpen.grothendieckTopology Y) :=
        SimplicialOpen.pullback_isMorphismOfSites f
    (levelFunctor X (op (SimplexCategory.mk n))).sheafPullbackCocontinuous
        (Type u) (Opens.grothendieckTopology (X.obj (op (SimplexCategory.mk n))))
        (SimplicialOpen.grothendieckTopology X) ⋙
      TopCat.Sheaf.pullback (Type u) (f.app (op (SimplexCategory.mk n))) ≅
    (SimplicialOpen.pullback f).sheafPullback
        (Type u) (SimplicialOpen.grothendieckTopology X)
        (SimplicialOpen.grothendieckTopology Y) ⋙
      (levelFunctor Y (op (SimplexCategory.mk n))).sheafPullbackCocontinuous
        (Type u) (Opens.grothendieckTopology (Y.obj (op (SimplexCategory.mk n))))
        (SimplicialOpen.grothendieckTopology Y)
```

## Tag 09W4, a lemma

[Tag 09W4](https://stacks.math.columbia.edu/tag/09W4) in the Stacks Project.

**`Stacks.Topology.Simplicial.augmentationMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/Augmentation.lean, line 621](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/Augmentation.lean#L621). The attribute's comment: “the canonical morphism of topoi”.

> The morphism from the topos of a simplicial space to that of its augmentation target,
> with the coherent component identifications from the construction in the source proof.

```lean
noncomputable def augmentationMorphism
    (a : Y ⟶ (SimplicialObject.const TopCat).obj X) :
    AugmentationMorphismData Y X a
```

**`Stacks.Topology.Simplicial.augmentationMorphism_inverseImage_component`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/Augmentation.lean, line 645](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/Augmentation.lean#L645). The attribute's comment: “part (1): inverse image on components”.

> **Stacks 09W4 (1).** Inverse image along the augmentation restricts in degree `n`
> to inverse image along the component map `a_n`.

```lean
noncomputable def augmentationMorphism_inverseImage_component
    (n : SimplexCategoryᵒᵖ) :
    (augmentationMorphism Y X a).inverseImage ⋙
      (sheafEquivalenceSimplicialSheafSystem Y (Type u)).toEquivalence.functor ⋙
        SimplicialSheafSystem.componentFunctor Y (Type u) n ≅
      TopCat.Sheaf.pullback (Type u) (a.app n)
```

**`Stacks.Topology.Simplicial.augmentationMorphism_inverseImage_transition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/Augmentation.lean, line 656](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/Augmentation.lean#L656). The attribute's comment: “part (1): compatibility of inverse-image transitions”.

> The inverse-image component isomorphisms intertwine every system transition with
> the canonical map between pullbacks induced by the augmentation equation.

```lean
theorem augmentationMorphism_inverseImage_transition (F : TopCat.Sheaf (Type u) X)
    {n m : SimplexCategoryᵒᵖ} (φ : n ⟶ m) (V : (Opens (Y.obj m))ᵒᵖ) :
    let S := (sheafEquivalenceSimplicialSheafSystem Y (Type u)).toEquivalence.functor.obj
      ((augmentationMorphism Y X a).inverseImage.obj F)
    (S.transition φ).app V ≫
        ((TopCat.Sheaf.forget (Type u) (Y.obj n)).map
          ((augmentationMorphism_inverseImage_component Y X a n).app F).hom).app
            (op ((Opens.map (Y.map φ)).obj V.unop)) =
      ((TopCat.Sheaf.forget (Type u) (Y.obj m)).map
        ((augmentationMorphism_inverseImage_component Y X a m).app F).hom).app V ≫
          (augmentationPullbackTransition Y X a F φ).app V
```

**`Stacks.Topology.Simplicial.augmentationMorphism_comp_component`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/Augmentation.lean, line 672](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/Augmentation.lean#L672). The attribute's comment: “part (3): composition with a component inclusion”.

> **Stacks 09W4 (3).** The composite of the component inclusion and the augmentation
> agrees with the topological morphism induced by `a_n`.

```lean
noncomputable def augmentationMorphism_comp_component (n : SimplexCategoryᵒᵖ) :
    (augmentationMorphism Y X a).inverseImage ⋙
      (levelFunctor Y n).sheafPullbackCocontinuous (Type u)
        (Opens.grothendieckTopology (Y.obj n))
        (SimplicialOpen.grothendieckTopology Y) ≅
      TopCat.Sheaf.pullback (Type u) (a.app n)
```

**`Stacks.Topology.Simplicial.augmentationMorphism_pushforwardEqualizer`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/Augmentation.lean, line 703](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/Augmentation.lean#L703). The attribute's comment: “part (4): direct image as an equalizer”.

> **Stacks 09W4 (4).** The direct image of a sheaf on the simplicial site is the
> equalizer of the two degree-one transition maps on direct images.

```lean
noncomputable def augmentationMorphism_pushforwardEqualizer
    (G : Sheaf (SimplicialOpen.grothendieckTopology Y) (Type u)) :
    (augmentationMorphism Y X a).pushforward.obj G ≅
      equalizer (augmentationFaceMap Y X a G 0) (augmentationFaceMap Y X a G 1)
```

Declarations registered for the tag:

- [`CategoryTheory.Limits.Cocone.w`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.Cocone.w#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Simplicial/Augmentation.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/Augmentation.lean#L70) (StacksFrontier): “part (2): compatibility of augmentation maps”.

## Tag 09W5, a lemma

[Tag 09W5](https://stacks.math.columbia.edu/tag/09W5) in the Stacks Project.

**`Stacks.Topology.Simplicial.freeAbelianRepresentableComplex_quasiIso_constant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/Resolution.lean, line 203](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/Resolution.lean#L203).

> **Stacks 09W5.** The alternating face-map complex of the free abelian presheaves represented
> by `X_n`, augmented towards the constant presheaf of integers, is a resolution in abelian
> presheaves.

```lean
theorem freeAbelianRepresentableComplex_quasiIso_constant
    (X : SimplicialObject TopCat.{u}) :
    QuasiIso (AlternatingFaceMapComplex.ε.app
      (augmentedFreeAbelianPresheaf X))
```

## Tag 09W6, a lemma

[Tag 09W6](https://stacks.math.columbia.edu/tag/09W6) in the Stacks Project.

**`Stacks.Topology.Simplicial.cohomologySpectralSequence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/CohomologySpectralSequence.lean, line 317](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/CohomologySpectralSequence.lean#L317). The attribute's comment: “the spectral sequence, functorial in the abelian sheaf”.

> **Stacks 09W6.**  For an abelian sheaf `F` on the site of a simplicial topological space `X`
> there is a first-quadrant cohomological spectral sequence, functorial in `F`: the second spectral
> sequence of the double complex `A^{q,p} = I^q(X_p)` of a chosen injective resolution of `F`,
> presented from its first page.  Its first page is `cohomologySpectralSequence_pageOneIso`, and its
> convergence to `H^{p+q}(X_Zar, F)` is `cohomologySpectralSequence_abutment`.

```lean
noncomputable def cohomologySpectralSequence :
    Sheaf (SimplicialOpen.grothendieckTopology X) Ab.{w} ⥤
      CohomologicalSpectralSequenceNat Ab.{w} 1
```

**`Stacks.Topology.Simplicial.cohomologySpectralSequence_pageOneIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/CohomologySpectralSequence.lean, line 614](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/CohomologySpectralSequence.lean#L614). The attribute's comment: “the first page is H^q(X\_p, F\_p)”.

> **Stacks 09W6.**  The first page of the spectral sequence of a simplicial topological space
> is `E_1^{p,q} = H^q(X_p, F_p)`, the sheaf cohomology of the restriction of `F` to the space in
> simplicial degree `p`, naturally in the abelian sheaf `F`.

```lean
noncomputable def cohomologySpectralSequence_pageOneIso (q : ℕ) :
    pageOneFunctor.{u, w} X n q ≅ componentCohomologyFunctor.{u, w} X n q
```

**`Stacks.Topology.Simplicial.cohomologySpectralSequence_abutment`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/CohomologySpectralSequenceAbutment.lean, line 1270](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/CohomologySpectralSequenceAbutment.lean#L1270). The attribute's comment: “convergence to H^\{p+q}(X\_Zar, F), functorially in the abelian sheaf”.

> **Stacks 09W6, the convergence.**  The spectral sequence of a simplicial topological space,
> with first page `E_1^{p,q} = H^q(X_p, F_p)`, converges to `H^{p+q}(X_Zar, F)`, functorially in the
> abelian sheaf `F`: for every `n` there is a finite decreasing filtration of
> `H^n(X_Zar, F) = R^nΓ(X_Zar, F)`, natural in `F`, which is the whole group in step `0` and zero in
> step `n + 1`, and whose graded pieces are naturally the terms `E_∞^{p,n-p}` of the infinity page.
>
> The filtration is the one the filtration of the total complex of `A^{q,p} = I^q(X_p)` by the
> simplicial degree induces on its cohomology (`simplicialFunctorialAbutment`); that cohomology is
> `H^n(X_Zar, F)` by `cohomologySpectralSequence_abutmentIso`.

```lean
def cohomologySpectralSequence_abutment :
    FunctorialFirstQuadrantAbutsTo (cohomologySpectralSequence.{u, w} X)
      (fun n => (Sheaf.Γ (SimplicialOpen.grothendieckTopology X) Ab.{w}).rightDerived n)
```

## Tag 0D84, a lemma

[Tag 0D84](https://stacks.math.columbia.edu/tag/0D84) in the Stacks Project.

**`Stacks.Topology.Simplicial.fibreRestrictionAb_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/AugmentationFibreCohomology.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/AugmentationFibreCohomology.lean#L117). The attribute's comment: “the proof's use of exactness of restriction to the fibre”.

> **Restriction of abelian sheaves to the fibre is exact.**

```lean
theorem fibreRestrictionAb_exact :
    exactFunctor (Sheaf (SimplicialOpen.grothendieckTopology X) Ab.{u})
      (Sheaf (SimplicialOpen.grothendieckTopology (fibreSpace X Y a V)) Ab.{u})
      (fibreRestrictionAb X Y a V)
```

**`Stacks.Topology.Simplicial.fibreRestrictedSections_rightDerived_iso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/AugmentationFibreCohomology.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/AugmentationFibreCohomology.lean#L185). The attribute's comment: “the proof's reduction: derived sections of the restriction are fibre cohomology”.

> **Stacks 0D84, the reduction step of the proof.** The `n`-th right derived functor of
> `F ↦ Γ((X ×_Y V)_Zar, F|)` is the cohomology `Hⁿ((X ×_Y V)_Zar, F|)` of the restriction.
>
> An injective resolution of `F` on `X_Zar` restricts to an injective resolution of `F|` on
> `(X ×_Y V)_Zar`, because restriction is exact (`fibreRestrictionAb_exact`) and carries
> injectives to injectives (part (1) of the source proof,
> `fibreRestrictionAb_preservesInjectiveObjects`); so one and the same complex computes both
> sides.

```lean
noncomputable def fibreRestrictedSections_rightDerived_iso (n : ℕ)
    (F : Sheaf (SimplicialOpen.grothendieckTopology X) Ab.{u}) :
    ((fibreRestrictedSections X Y a V).rightDerived n).obj F ≅
      (fibreCohomology X Y a V n).obj ((fibreRestrictionAb X Y a V).obj F)
```

**`Stacks.Topology.Simplicial.fibreRestrictionAb_preservesInjectiveObjects`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/AugmentationFibreInjectives.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/AugmentationFibreInjectives.lean#L141). The attribute's comment: “part (1) of the proof: restriction to the fibre preserves injectives”.

> **Stacks 0D84, part (1) of the proof.** The restriction of an abelian sheaf on `X_Zar` to
> `(X ×_Y V)_Zar` preserves injective objects: its left adjoint, extension by zero, is exact, and
> a right adjoint of a functor preserving monomorphisms preserves injectives
> ([Stacks, Tag 015Z]).

```lean
theorem fibreRestrictionAb_preservesInjectiveObjects :
    (fibreRestrictionAb X Y a V).PreservesInjectiveObjects
```

**`Stacks.Topology.Simplicial.injective_fibreRestrictionAb_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/AugmentationFibreInjectives.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/AugmentationFibreInjectives.lean#L149). The attribute's comment: “part (1) of the proof: the restriction of an injective is injective”.

> **Stacks 0D84, part (1) of the proof.** The restriction to `(X ×_Y V)_Zar` of an injective
> abelian sheaf on `X_Zar` is an injective abelian sheaf.

```lean
theorem injective_fibreRestrictionAb_obj
    (I : Sheaf (SimplicialOpen.grothendieckTopology X) Ab.{u}) [Injective I] :
    Injective ((fibreRestrictionAb X Y a V).obj I)
```

**`Stacks.Topology.Simplicial.augmentationCohomologyPresheaf_obj_iso_fibreCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/AugmentationFibreMain.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/AugmentationFibreMain.lean#L66). The attribute's comment: “the values of the displayed presheaf are the cohomology of the fibre”.

> **Stacks 0D84.** The value over an open `V` of the target of the cohomology presheaf of an
> augmentation is the cohomology `Hⁿ((X ×_Y V)_Zar, F|)` of the restriction of `F` to the total
> site of the fibre `X ×_Y V`.
>
> This is the displayed rule of the statement.  Three steps: the value of the cohomology presheaf
> over `V` is the `n`-th right derived functor of the sections of the direct image over `V`
> (exactness of evaluation); those sections are the global sections of the restriction to the
> fibre, which is part (2) of the source proof; and the derived functors of the global sections of
> the restriction are the cohomology of the fibre, because restriction is exact and carries
> injectives to injectives, which is part (1) of the source proof.

```lean
theorem augmentationCohomologyPresheaf_obj_iso_fibreCohomology (n : ℕ)
    (F : Sheaf (SimplicialOpen.grothendieckTopology X) Ab.{u}) :
    Nonempty (((augmentationCohomologyPresheaf X Y a n).obj F).obj (op V) ≅
      (fibreCohomology X Y a V n).obj ((fibreRestrictionAb X Y a V).obj F))
```

**`Stacks.Topology.Simplicial.higherDirectImage_iso_sheafify_fibreCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/AugmentationFibreMain.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/AugmentationFibreMain.lean#L81).

> **Stacks 0D84.** Let `X` be a simplicial space, let `a : X ⟶ Y` be an augmentation and let
> `F` be an abelian sheaf on `X_Zar`.  Then `Rⁿa_*F` is the sheaf associated to the presheaf whose
> value over an open `V` of `Y` is `Hⁿ((X ×_Y V)_Zar, F|_{(X ×_Y V)_Zar})`.

```lean
theorem higherDirectImage_iso_sheafify_fibreCohomology (n : ℕ)
    (F : Sheaf (SimplicialOpen.grothendieckTopology X) Ab.{u}) :
    Nonempty (((augmentationPushforwardAb X Y a).rightDerived n).obj F ≅
        (presheafToSheaf (Opens.grothendieckTopology Y) Ab.{u}).obj
          ((augmentationCohomologyPresheaf X Y a n).obj F)) ∧
      ∀ V : Opens Y,
        Nonempty (((augmentationCohomologyPresheaf X Y a n).obj F).obj (op V) ≅
          (fibreCohomology X Y a V n).obj ((fibreRestrictionAb X Y a V).obj F))
```

**`Stacks.Topology.Simplicial.augmentationFibreSections_iso_fibreRestrictedSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/AugmentationFibrePartTwo.lean, line 343](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/AugmentationFibrePartTwo.lean#L343). The attribute's comment: “part (2) of the proof: the direct image over V is the sections over the fibre”.

> **Stacks 0D84, part (2) of the proof.** The sections over `V` of the direct image of an
> abelian sheaf `F` on `X_Zar` along an augmentation are the global sections over the total site of
> the fibre `X ×_Y V` of the restriction of `F`, naturally in `F`.

```lean
noncomputable def augmentationFibreSections_iso_fibreRestrictedSections :
    augmentationFibreSections X Y a V ≅ fibreRestrictedSections X Y a V
```

**`Stacks.Topology.Simplicial.higherDirectImage_iso_sheafify_augmentationCohomologyPresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/AugmentationHigherDirectImage.lean, line 198](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/AugmentationHigherDirectImage.lean#L198). The attribute's comment: “the sheafification of the cohomology presheaf; not its fibrewise values”.

> **Stacks 0D84.** Let `X` be a simplicial space, let `a : X ⟶ Y` be an augmentation and let
> `F` be an abelian sheaf on `X_Zar`.  Then the `n`-th higher direct image `Rⁿa_*F` is the sheaf
> associated to the cohomology presheaf of the augmentation, whose value over an open `V` of `Y`
> is `Hⁿ((X ×_Y V)_Zar, F|_{(X ×_Y V)_Zar})`.
>
> Sheafification is exact, so it commutes with the right derived functors of the presheaf-valued
> direct image; the higher direct image is the right derived functor of the sheaf-valued one,
> which is the sheafification of the presheaf-valued one.

```lean
theorem higherDirectImage_iso_sheafify_augmentationCohomologyPresheaf (n : ℕ)
    (F : Sheaf (SimplicialOpen.grothendieckTopology X) Ab.{u}) :
    Nonempty (((augmentationPushforwardAb X Y a).rightDerived n).obj F ≅
      (presheafToSheaf (Opens.grothendieckTopology Y) Ab.{u}).obj
        ((augmentationCohomologyPresheaf X Y a n).obj F))
```

**`Stacks.Topology.Simplicial.augmentationCohomologyPresheaf_evaluation_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/AugmentationHigherDirectImage.lean, line 220](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/AugmentationHigherDirectImage.lean#L220). The attribute's comment: “those values as derived sections of the direct image, not as fibre cohomology”.

> **Stacks 0D84.** The value over an open `V` of the target of the cohomology presheaf of an
> augmentation is the `n`-th right derived functor of the sections of the direct image over `V`.
> By part (2) of the source proof the latter functor is `F ↦ H⁰((X ×_Y V)_Zar, F|)`, so this is
> the displayed rule `V ↦ Hⁿ((X ×_Y V)_Zar, F|)` of the statement.
>
> Evaluation of a presheaf of abelian groups at an open is exact, so it commutes with right
> derived functors.

```lean
theorem augmentationCohomologyPresheaf_evaluation_iso (n : ℕ)
    (F : Sheaf (SimplicialOpen.grothendieckTopology X) Ab.{u}) (V : Opens Y) :
    Nonempty (((augmentationCohomologyPresheaf X Y a n).obj F).obj (op V) ≅
      ((augmentationFibreSections X Y a V).rightDerived n).obj F)
```

**`Stacks.Topology.Simplicial.augmentationPushforwardAb_forget_isoEqualizer`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/AugmentationHigherDirectImage.lean, line 240](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/AugmentationHigherDirectImage.lean#L240). The attribute's comment: “degree zero: the direct image as an equalizer of fibrewise direct images”.

> **Stacks 0D84, part (2a) of the proof.** The underlying sheaf of sets of the direct image
> `a_*F` of an abelian sheaf along an augmentation is the equalizer of the two maps induced by
> the vertices of the one-simplex between the direct images of the degree-zero and the
> degree-one components of `F`.
>
> Over an open `V` of the target the two sheaves of that equalizer have sections the sections of
> `F` over the simplicial opens `a_0⁻¹(V)` and `a_1⁻¹(V)`, which are the degree-zero and
> degree-one components of the simplicial space `X ×_Y V`.  This is the fibrewise description of
> the sections of `a_*F` used in the source proof.

```lean
def augmentationPushforwardAb_forget_isoEqualizer
    (F : Sheaf (SimplicialOpen.grothendieckTopology X) Ab.{u}) :
    (sheafCompose (Opens.grothendieckTopology Y) (forget Ab.{u})).obj
        ((augmentationPushforwardAb X Y a).obj F) ≅
      equalizer
        (augmentationFaceMap X Y a
          ((sheafCompose (SimplicialOpen.grothendieckTopology X) (forget Ab.{u})).obj F) 0)
        (augmentationFaceMap X Y a
          ((sheafCompose (SimplicialOpen.grothendieckTopology X) (forget Ab.{u})).obj F) 1)
```

## Tag 09W3, a lemma

[Tag 09W3](https://stacks.math.columbia.edu/tag/09W3) in the Stacks Project.

**`Stacks.Topology.Simplicial.constantSiteFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/ConstantSpace.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/ConstantSpace.lean#L70). The attribute's comment: “the functor on sites”.

> The functor from the simplicial-open site of the constant simplicial space to
> the site of open subsets of its value.

```lean
def constantSiteFunctor (X : TopCat.{u}) :
    SimplicialOpen (constantSpace X) ⥤ Opens X
```

**`Stacks.Topology.Simplicial.constantSiteFunctor_isContinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/ConstantSpace.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/ConstantSpace.lean#L117). The attribute's comment: “the functor is continuous”.

> The constant-site functor preserves sheaves.

```lean
theorem constantSiteFunctor_isContinuous (X : TopCat.{u}) :
    (constantSiteFunctor X).IsContinuous
      (SimplicialOpen.grothendieckTopology (constantSpace X))
      (Opens.grothendieckTopology X)
```

**`Stacks.Topology.Simplicial.constantSiteFunctor_isCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/ConstantSpace.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/ConstantSpace.lean#L130). The attribute's comment: “the functor is cocontinuous”.

> The constant-site functor lifts covers.

```lean
theorem constantSiteFunctor_isCocontinuous (X : TopCat.{u}) :
    (constantSiteFunctor X).IsCocontinuous
      (SimplicialOpen.grothendieckTopology (constantSpace X))
      (Opens.grothendieckTopology X)
```

**`Stacks.Topology.Simplicial.constantMorphism_inverseImage_isoRestriction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/ConstantSpace.lean, line 359](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/ConstantSpace.lean#L359). The attribute's comment: “inverse image is restriction along the functor”.

> The canonical morphism has inverse image given by restriction along the
> constant-site functor, naturally in the sheaf.

```lean
noncomputable def constantMorphism_inverseImage_isoRestriction (X : TopCat.{u}) :
    (constantMorphism X).inverseImage ≅
    (constantSiteFunctor X).sheafPushforwardContinuous (Type u)
        (SimplicialOpen.grothendieckTopology (constantSpace X))
        (Opens.grothendieckTopology X)
```

**`Stacks.Topology.Simplicial.constantMorphism_inverseImage_component`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/ConstantSpace.lean, line 376](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/ConstantSpace.lean#L376). The attribute's comment: “part (1): constant cosimplicial inverse image”.

> Inverse image of a sheaf is the same sheaf in every simplicial degree,
> naturally in the sheaf.

```lean
noncomputable def constantMorphism_inverseImage_component (X : TopCat.{u})
    (n : SimplexCategoryᵒᵖ) :
    (constantMorphism X).inverseImage ⋙
      (sheafEquivalenceSimplicialSheafSystem (constantSpace X)
        (Type u)).toEquivalence.functor ⋙
        SimplicialSheafSystem.componentFunctor (constantSpace X) (Type u) n ≅
      𝟭 (TopCat.Sheaf (Type u) X)
```

**`Stacks.Topology.Simplicial.constantMorphism_inverseImage_transition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/ConstantSpace.lean, line 388](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/ConstantSpace.lean#L388). The attribute's comment: “part (1): constant transition maps”.

> The component identifications respect every cosimplicial transition: the
> transition maps of inverse image become identity maps of the original sheaf.

```lean
theorem constantMorphism_inverseImage_transition (X : TopCat.{u})
    (F : TopCat.Sheaf (Type u) X) {n m : SimplexCategoryᵒᵖ} (φ : n ⟶ m)
    (V : (Opens X)ᵒᵖ) :
    let S := (sheafEquivalenceSimplicialSheafSystem (constantSpace X)
        (Type u)).toEquivalence.functor.obj
        ((constantMorphism X).inverseImage.obj F)
    (S.transition φ).app V ≫
      ((TopCat.Sheaf.forget (Type u) X).map
        ((constantMorphism_inverseImage_component X n).app F).hom).app V =
      ((TopCat.Sheaf.forget (Type u) X).map
        ((constantMorphism_inverseImage_component X m).app F).hom).app V
```

**`Stacks.Topology.Simplicial.constantLowerShriek`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/ConstantSpace.lean, line 403](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/ConstantSpace.lean#L403). The attribute's comment: “part (2): lower shriek is the degree-zero component”.

> Lower shriek takes the degree-zero sheaf.

```lean
def constantLowerShriek (X : TopCat.{u}) :
    Sheaf (SimplicialOpen.grothendieckTopology (constantSpace X)) (Type u) ⥤
      TopCat.Sheaf (Type u) X
```

**`Stacks.Topology.Simplicial.constantLowerShriek_adjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/ConstantSpace.lean, line 433](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/ConstantSpace.lean#L433). The attribute's comment: “the lower-shriek adjunction”.

> **Stacks 09W3.** Lower shriek is left adjoint to the inverse image of the constant
> morphism.

```lean
noncomputable def constantLowerShriek_adjunction (X : TopCat.{u}) :
    constantLowerShriek X ⊣ (constantMorphism X).inverseImage
```

**`Stacks.Topology.Simplicial.constantMorphism_pushforwardEqualizer`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/ConstantSpace.lean, line 463](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/ConstantSpace.lean#L463). The attribute's comment: “part (3): direct image as an equalizer”.

> The direct image of a sheaf on the constant simplicial space is the
> equalizer of its two vertex transition maps from degree zero to degree one.

```lean
noncomputable def constantMorphism_pushforwardEqualizer (X : TopCat.{u})
    (G : Sheaf (SimplicialOpen.grothendieckTopology (constantSpace X)) (Type u)) :
    (constantMorphism X).pushforward.obj G ≅
      equalizer (constantFaceMap X G 0) (constantFaceMap X G 1)
```

Declarations registered for the tag:

- [`augmentationMorphism`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=augmentationMorphism#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Simplicial/ConstantSpace.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Simplicial/ConstantSpace.lean#L61) (StacksFrontier): “the morphism of topoi”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 85.2, Tag 09VK](https://stacks.math.columbia.edu/tag/09VK)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
