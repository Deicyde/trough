---
declaration: module
origin: cited
lean: ACCSystemCharges, ACCSystemCharges.Charges, ACCSystemCharges.chargesAddCommMonoid, ACCSystemCharges.chargesModule, ACCSystemCharges.ChargesAddCommGroup, ACCSystemLinear, ACCSystemLinear.LinSols, ACCSystemLinear.LinSols.ext
statement: formalized
proof: formalized
---

# Anomaly cancellation conditions

The module `Physlib.QFT.AnomalyCancellation.Basic`, [Physlib/QFT/AnomalyCancellation/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean): 36 declarations (1 instance with no name), 28 with a docstring.

## i. Overview

> Anomaly cancellation conditions (ACCs) are consistency conditions which arise
> in gauge field theories. They correspond to a set of homogeneous diophantine equations
> in the rational charges assigned to fermions under `u(1)` contributions to the gauge group.
>
> These formally arise from triangle Feynman diagrams, but can otherwise be got from
> index theorems.

## ii. Key results

> There are four different types related to the underlying structure of
> the ACCs:
> - `ACCSystemCharges`: the structure carrying the number of charges present.
> - `ACCSystemLinear`: the structure extending `ACCSystemCharges` with linear anomaly cancellation
>   conditions.
> - `ACCSystemQuad`: the structure extending `ACCSystemLinear` with quadratic anomaly cancellation
>   conditions.
> - `ACCSystem`: the structure extending `ACCSystemQuad` with the cubic anomaly cancellation
>   condition.
>
> Related to these are the different types of spaces of charges:
> - `Charges`: the module of all possible charge allocations.
> - `LinSols`: the module of solutions to the linear ACCs.
> - `QuadSols`: the solutions to the linear and quadratic ACCs.
> - `Sols`: the solutions to the full ACCs.

## iv. References

> * Alvarez-Gaume, L. and Ginsparg, P. H. (1985). The Structure of Gauge and Gravitational Anomalies.
>   [ref: alvarez\_gaume\_ginsparg\_1985]
> * Bilal, A. (2008). Lectures on Anomalies. arXiv preprint. [ref: bilal\_2008\_anomalies]
> * Nash, C. (1991). Differential topology and quantum field theory. Elsevier. [ref: nash\_1991\_dtqft]

## A. The module of charges

> We define the type `ACCSystemCharges`, this carries the charges
> of the specification of the number of charges present in a theory.
>
> For example for the standard model without right-handed neutrinos, this is `15` charges,
> whilst with right handed neutrinos it is `18` charges.
>
> We can think of `Fin χ.numberCharges` as an indexing type for
> the representations present in the theory where `χ : ACCSystemCharges`.

**`ACCSystemCharges`**, a structure, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean#L98).

> A system of charges, specified by the number of charges.

```lean
structure ACCSystemCharges where
  /-- The number of charges. -/
  numberCharges : ℕ
```

## B. The module of charges

> Given an `ACCSystemCharges` object `χ`, we define the type of charges
> `χ.Charges` as functions from `Fin χ.numberCharges → ℚ`.
>
> That is, for each representation in the theory, indexed by an element of `Fin χ.numberCharges`,
> we assign a rational charge.

**`ACCSystemCharges.Charges`**, a def, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean#L117).

> The charges as functions from `Fin χ.numberCharges → ℚ`.

```lean
def Charges (χ : ACCSystemCharges) : Type
```

### B.1. The `ℚ`-module structure on the type `Charges`

> The type `χ.Charges` has the structure of a module over the field `ℚ`.

**`ACCSystemCharges.chargesAddCommMonoid`**, an instance, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean#L132).

> An instance to provide the necessary operations and properties for `charges` to form an additive
> commutative monoid.

```lean
instance chargesAddCommMonoid (χ : ACCSystemCharges) : AddCommMonoid χ.Charges
```

**`ACCSystemCharges.chargesModule`**, an instance, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean#L140).

> An instance to provide the necessary operations and properties for `charges` to form a module
> over the field `ℚ`.

```lean
instance chargesModule (χ : ACCSystemCharges) : Module ℚ χ.Charges
```

**`ACCSystemCharges.ChargesAddCommGroup`**, an instance, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean#L143).

```lean
instance ChargesAddCommGroup (χ : ACCSystemCharges) : AddCommGroup χ.Charges
```

### B.2. The finiteness of the `ℚ`-module structure on `Charges`

> The type `χ.Charges` is a finite module.

**An instance with no name**, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean#L155).

> The module `χ.Charges` over `ℚ` is finite.

```lean
instance (χ : ACCSystemCharges) : Module.Finite ℚ χ.Charges
```

## C. The linear anomaly cancellation conditions

> We define the type `ACCSystemLinear` which extends `ACCSystemCharges` by adding
> a finite number (determined by `numberLinear`) of linear equations in the rational charges.

**`ACCSystemLinear`**, a structure, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean#L170).

> The type of charges plus the linear ACCs.

```lean
structure ACCSystemLinear extends ACCSystemCharges where
  /-- The number of linear ACCs. -/
  numberLinear : ℕ
  /-- The linear ACCs. -/
  linearACCs : Fin numberLinear → (toACCSystemCharges.Charges →ₗ[ℚ] ℚ)
```

## D. The module of solutions to the linear ACCs

> We define the type `LinSols` of solutions to the linear ACCs.
> That is the submodule of `χ.Charges` which satisfy all the linear ACCs.

**`ACCSystemLinear.LinSols`**, a structure, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean#L188).

> The type of solutions to the linear ACCs.

```lean
structure LinSols (χ : ACCSystemLinear) where
  /-- The underlying charge. -/
  val : χ.1.Charges
  /-- The condition that the charge satisfies the linear ACCs. -/
  linearSol : ∀ i : Fin χ.numberLinear, χ.linearACCs i val = 0
```

### D.1. Extensionality of solutions to the linear ACCs

> We prove a lemma relating to the equality of two elements of `LinSols`.

**`ACCSystemLinear.LinSols.ext`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean#L204).

> Two solutions are equal if the underlying charges are equal.

```lean
lemma LinSols.ext {χ : ACCSystemLinear} {S T : χ.LinSols} (h : S.val = T.val) : S = T
```

### D.2. Module structure on the solutions to the linear ACCs

> we now give a module structure to `LinSols`.

**`ACCSystemLinear.linSolsAddCommMonoid`**, an instance, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean#L219).

> An instance providing the operations and properties for `LinSols` to form an
> additive commutative monoid.

```lean
instance linSolsAddCommMonoid (χ : ACCSystemLinear) :
    AddCommMonoid χ.LinSols
```

**`ACCSystemLinear.linSolsModule`**, an instance, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean#L235).

> An instance providing the operations and properties for `LinSols` to form a
> module over `ℚ`.

```lean
instance linSolsModule (χ : ACCSystemLinear) : Module ℚ χ.LinSols
```

**`ACCSystemLinear.linSolsAddCommGroup`**, an instance, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean#L244).

```lean
instance linSolsAddCommGroup (χ : ACCSystemLinear) : AddCommGroup χ.LinSols
```

### D.3. Embedding of the solutions to the linear ACCs into the module of charges

> We give the linear embedding of solutions to the linear ACCs `LinSols` into
> the module of all `charges`.

**`ACCSystemLinear.linSolsIncl`**, a def, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean#L257).

> The inclusion of `LinSols` into `charges`.

```lean
def linSolsIncl (χ : ACCSystemLinear) : χ.LinSols →ₗ[ℚ] χ.Charges
```

**`ACCSystemLinear.linSolsIncl_injective`**, a lemma, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean#L262).

```lean
lemma linSolsIncl_injective (χ : ACCSystemLinear) :
    Function.Injective χ.linSolsIncl
```

## E. The quadratic anomaly cancellation conditions

> We extend `ACCSystemLinear` to `ACCSystemQuad` by adding a finite number
> (determined by `numberQuadratic`) of quadratic equations in the rational charges.
>
> These quadratic anomaly cancellation conditions correspond to the interaction
> of the `u(1)` part of the gauge group of interest with another abelian part.

**`ACCSystemQuad`**, a structure, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean#L280).

> The type of charges plus the linear ACCs plus the quadratic ACCs.

```lean
structure ACCSystemQuad extends ACCSystemLinear where
  /-- The number of quadratic ACCs. -/
  numberQuadratic : ℕ
  /-- The quadratic ACCs. -/
  quadraticACCs : Fin numberQuadratic → HomogeneousQuadratic toACCSystemCharges.Charges
```

## F. The solutions to the quadratic and linear anomaly cancellation conditions

> We define the type `QuadSols` of solutions to the linear and quadratic ACCs.

**`ACCSystemQuad.QuadSols`**, a structure, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean#L297).

> The type of solutions to the linear and quadratic ACCs.

```lean
structure QuadSols (χ : ACCSystemQuad) extends χ.LinSols where
  /-- The condition that the charge satisfies the quadratic ACCs. -/
  quadSol : ∀ i : Fin χ.numberQuadratic, (χ.quadraticACCs i) val = 0
```

### F.1. Extensionality of solutions to the quadratic and linear ACCs

> We prove a lemma relating to the equality of two elements of `QuadSols`.

**`ACCSystemQuad.QuadSols.ext`**, a lemma, [line 311](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean#L311).

> Two `QuadSols` are equal if the underlying charges are equal.

```lean
lemma QuadSols.ext {χ : ACCSystemQuad} {S T : χ.QuadSols} (h : S.val = T.val) :
    S = T
```

### F.2. MulAction of rationals on the solutions to the quadratic and linear ACCs

> The type `QuadSols` does not carry the structure of a module over `ℚ` as
> the quadratic ACCs are not linear. However it does carry the structure of
> a `MulAction` of `ℚ`.

**`ACCSystemQuad.quadSolsMulAction`**, an instance, [line 327](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean#L327).

> An instance giving the properties and structures to define an action of `ℚ` on `QuadSols`.

```lean
instance quadSolsMulAction (χ : ACCSystemQuad) : MulAction ℚ χ.QuadSols
```

### F.3. Embeddings of quadratic solutions into linear solutions

> We give the equivariant of solutions to the quadratic and linear ACCs `QuadSols` into
> the solutions to the linear ACCs `LinSols`.

**`ACCSystemQuad.quadSolsInclLinSols`**, a def, [line 343](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean#L343).

> The inclusion of quadratic solutions into linear solutions.

```lean
def quadSolsInclLinSols (χ : ACCSystemQuad) : χ.QuadSols →[ℚ] χ.LinSols
```

**`ACCSystemQuad.quadSolsInclLinSols_injective`**, a lemma, [line 347](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean#L347).

```lean
lemma quadSolsInclLinSols_injective (χ : ACCSystemQuad) :
    Function.Injective χ.quadSolsInclLinSols
```

### F.4. Embeddings of solutions to linear ACCs into quadratic solutions when no quadratics

> When there are no quadratic ACCs, the solutions to the linear ACCs embed into the solutions
> to the quadratic and linear ACCs.

**`ACCSystemQuad.linSolsInclQuadSolsZero`**, a def, [line 362](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean#L362).

> The inclusion of the linear solutions into the quadratic solutions, where there is
> no quadratic equations (i.e. no U(1)'s in the underlying gauge group).

```lean
def linSolsInclQuadSolsZero (χ : ACCSystemQuad) (h : χ.numberQuadratic = 0) :
    χ.LinSols →[ℚ] χ.QuadSols
```

### F.5. Embeddings of quadratic solutions into all charges

> We give the equivariant embedding of solutions to the quadratic and linear ACCs `QuadSols` into
> the module of all charges `Charges`.

**`ACCSystemQuad.quadSolsIncl`**, a def, [line 377](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean#L377).

> The inclusion of quadratic solutions into all charges.

```lean
def quadSolsIncl (χ : ACCSystemQuad) : χ.QuadSols →[ℚ] χ.Charges
```

**`ACCSystemQuad.quadSolsIncl_injective`**, a lemma, [line 380](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean#L380).

```lean
lemma quadSolsIncl_injective (χ : ACCSystemQuad) :
    Function.Injective χ.quadSolsIncl
```

## G. The full anomaly cancellation conditions

> We extend `ACCSystemQuad` to `ACCSystem` by adding the single cubic equation
> in the rational charges. This corresponds to the `u(1)^3` anomaly.

**`ACCSystem`**, a structure, [line 406](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean#L406).

> The type of charges plus the anomaly cancellation conditions.
>
> In many physical settings these conditions are derived formally from the gauge group and the
> fermionic representations. They arise from triangle Feynman diagrams, and can also be obtained
> using index-theoretic or characteristic-class constructions.
>
> In this file, we take the resulting conditions as input data: linear, quadratic and cubic
> homogeneous forms on the space of rational charges.

```lean
structure ACCSystem extends ACCSystemQuad where
  /-- The cubic ACC. -/
  cubicACC : HomogeneousCubic toACCSystemCharges.Charges
```

## H. The solutions to the full anomaly cancellation conditions

> We define the type `Sols` of solutions to the full ACCs.

**`ACCSystem.Sols`**, a structure, [line 421](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean#L421).

> The type of solutions to the anomaly cancellation conditions.

```lean
structure Sols (χ : ACCSystem) extends χ.QuadSols where
  /-- The condition that the charge satisfies the cubic ACC. -/
  cubicSol : χ.cubicACC val = 0
```

### H.1. Extensionality of solutions to the ACCs

> We prove a lemma relating to the equality of two elements of `Sols`.

**`ACCSystem.Sols.ext`**, a lemma, [line 434](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean#L434).

> Two solutions are equal if the underlying charges are equal.

```lean
lemma Sols.ext {χ : ACCSystem} {S T : χ.Sols} (h : S.val = T.val) :
    S = T
```

### H.2. The `IsSolution` predicate

> we define a predicate on charges which is true if they correspond to a solution.

**`ACCSystem.IsSolution`**, a def, [line 449](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean#L449).

> A charge `S` is a solution if it extends to a solution.

```lean
def IsSolution (χ : ACCSystem) (S : χ.Charges) : Prop
```

### H.3. MulAction of `ℚ` on the solutions to the ACCs

> Like with `QuadSols`, the type `Sols` does not carry the structure of a module over `ℚ`
> as the cubic nor quadratic ACC is not linear. However it does carry the structure of
> a `MulAction` of `ℚ`.

**`ACCSystem.solsMulAction`**, an instance, [line 463](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean#L463).

> An instance giving the properties and structures to define an action of `ℚ` on `Sols`.

```lean
instance solsMulAction (χ : ACCSystem) : MulAction ℚ χ.Sols
```

### H.4. Embeddings of solutions to the ACCs into quadratic solutions

**`ACCSystem.solsInclQuadSols`**, a def, [line 477](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean#L477).

> The inclusion of `Sols` into `QuadSols`.

```lean
def solsInclQuadSols (χ : ACCSystem) : χ.Sols →[ℚ] χ.QuadSols
```

**`ACCSystem.solsInclQuadSols_injective`**, a lemma, [line 481](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean#L481).

```lean
lemma solsInclQuadSols_injective (χ : ACCSystem) :
    Function.Injective χ.solsInclQuadSols
```

### H.5. Embeddings of solutions to the ACCs into linear solutions

**`ACCSystem.solsInclLinSols`**, a def, [line 491](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean#L491).

> The inclusion of `Sols` into `LinSols`.

```lean
def solsInclLinSols (χ : ACCSystem) : χ.Sols →[ℚ] χ.LinSols
```

**`ACCSystem.solsInclLinSols_injective`**, a lemma, [line 494](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean#L494).

```lean
lemma solsInclLinSols_injective (χ : ACCSystem) :
    Function.Injective χ.solsInclLinSols
```

### H.6. Embeddings of solutions to the ACCs into charges

**`ACCSystem.solsIncl`**, a def, [line 506](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean#L506).

> The inclusion of `Sols` into `LinSols`.

```lean
def solsIncl (χ : ACCSystem) : χ.Sols →[ℚ] χ.Charges
```

**`ACCSystem.solsIncl_injective`**, a lemma, [line 509](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean#L509).

```lean
lemma solsIncl_injective (χ : ACCSystem) :
    Function.Injective χ.solsIncl
```

## I. Morphisms between ACC systems

> We define a morphisms between two `ACCSystem` objects.
> as a linear map between their spaces of charges and a map between their spaces of solutions
> such that mapping solutions and then including in the module of charges
> is the same as including in the module of charges and then mapping charges.

**`ACCSystem.Hom`**, a structure, [line 526](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean#L526).

> The structure of a map between two ACCSystems.

```lean
structure Hom (χ η : ACCSystem) where
  /-- The linear map between vector spaces of charges. -/
  charges : χ.Charges →ₗ[ℚ] η.Charges
  /-- The map between solutions. -/
  anomalyFree : χ.Sols → η.Sols
  /-- The condition that the map commutes with the relevant inclusions. -/
  commute : charges ∘ χ.solsIncl = η.solsIncl ∘ anomalyFree
```

### I.1. Composition of morphisms between ACC systems

**`ACCSystem.Hom.comp`**, a def, [line 541](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean#L541).

> The definition of composition between two ACCSystems.

```lean
def Hom.comp {χ η ε : ACCSystem} (g : Hom η ε) (f : Hom χ η) : Hom χ ε
```

…

## Depends on

- [Linear maps](../../mathematics/formathlib/linearmaps.md)

## Sources

- [Physlib/QFT/AnomalyCancellation/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/AnomalyCancellation/Basic.lean)
