---
catalog: module
lean: Cslib.RelationAlgebra.IntegralAtom, Cslib.RelationAlgebra.IntegralAtom.equivOptionSum, Cslib.RelationAlgebra.IntegralAtom.conv, Cslib.RelationAlgebra.IntegralAtom.Cycle, Cslib.RelationAlgebra.IntegralAtom.Cycle.left, Cslib.RelationAlgebra.IntegralAtom.Cycle.right, Cslib.RelationAlgebra.IntegralAtom.Cycle.IsDiversity, Cslib.RelationAlgebra.IntegralAtom.CycleClosure, Cslib.RelationAlgebra.IntegralAtom.conv_one, Cslib.RelationAlgebra.IntegralAtom.conv_symm, Cslib.RelationAlgebra.IntegralAtom.conv_nsymm, Cslib.RelationAlgebra.IntegralAtom.conv_conv, Cslib.RelationAlgebra.IntegralAtom.CycleClosure.id_cycle_left, Cslib.RelationAlgebra.IntegralAtom.CycleClosure.id_cycle_right, Cslib.RelationAlgebra.IntegralAtom.CycleClosure.id_cycle_conv, Cslib.RelationAlgebra.IntegralAtom.cycleClosure_one_iff, Cslib.RelationAlgebra.IntegralAtom.ofCycles, Cslib.RelationAlgebra.IntegralAtom.ofCycles_conv, Cslib.RelationAlgebra.IntegralAtom.mem_ofCycles_id, Cslib.RelationAlgebra.IntegralAtom.mem_ofCycles_cycles, Cslib.RelationAlgebra.IntegralAtom.lawfulAtomStructure_ofCycles, Cslib.RelationAlgebra.IntegralAtom.isIntegral_ofCycles, Cslib.RelationAlgebra.IntegralAtom.preimage_singleton_symmetricDiversityAtoms, Cslib.RelationAlgebra.IntegralAtom.preimage_singleton_nonsymmetricDiversityAtoms, Cslib.RelationAlgebra.IntegralAtom.ncard_symmetricDiversityAtoms_ofCycles, Cslib.RelationAlgebra.IntegralAtom.ncard_nonsymmetricDiversityAtoms_ofCycles, Cslib.RelationAlgebra.IntegralAtom.setoid, Cslib.RelationAlgebra.IntegralAtom.IsoClass.ofSymmNsymm, Cslib.RelationAlgebra.IntegralAtom.IsoClass.ofAtoms, Cslib.RelationAlgebra.IntegralAtom.IsoClass.isEmpty_ofAtoms_zero, Cslib.RelationAlgebra.IntegralAtom.IsoClass.card_ofAtoms_succ_eq_sum_ofSymmNsymm
statement: formalized
proof: formalized
---

# Integral atom structures

`Cslib.Foundations.RelationAlgebra.IntegralAtomStructure`, in [Cslib/Foundations/RelationAlgebra/IntegralAtomStructure.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/IntegralAtomStructure.lean), by Chris Henson.

> This module abstractly defines the atoms of an integral relation algebra, along with a
> characterization of its identity and non-identity cycles that form an atom structure when
> shown to be associative.
>
> ## References
>
> * [Steven Givant, *Introduction to Relation Algebras*][Givant2017a], Section 4.2
> * [Steven Givant, *Advanced Topics in Relation Algebras*][Givant2017b], Section 19.3
> * [Peter Jipsen, *Small relation algebras*](https://www1.chapman.edu/~jipsen/gap/ramaddux.html)

`Cslib.RelationAlgebra.IntegralAtom` (inductive type, [line 35](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/IntegralAtomStructure.lean#L35))

> The atoms of an integral atom structure: the identity atom, a type `α` of symmetric diversity atoms,
> and a type `β` of pairs of nonsymmetric atoms.

```lean
inductive IntegralAtom (α β : Type*) where
  /-- The identity atom. -/
  | one
  /-- A symmetric diversity atom. -/
  | symm (a : α)
  /-- A nonsymmetric atom. `nsymm b true` is the converse of `nsymm b false`. -/
  | nsymm (b : β) (conv : Bool)
  deriving DecidableEq
```

`Cslib.RelationAlgebra.IntegralAtom.equivOptionSum` (definition, [line 49](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/IntegralAtomStructure.lean#L49))

> `IntegralAtom α β` as a sum.

```lean
def equivOptionSum : IntegralAtom α β ≃ Option (α ⊕ β × Bool)
```

`Cslib.RelationAlgebra.IntegralAtom.conv` (definition, [line 64](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/IntegralAtomStructure.lean#L64))

> The converse of an atom, where just nonsymmetric atoms are flipped.

```lean
def conv : IntegralAtom α β → IntegralAtom α β
```

`Cslib.RelationAlgebra.IntegralAtom.Cycle` (abbreviation, [line 70](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/IntegralAtomStructure.lean#L70))

> An integral cycle is a triple of integral atoms.

```lean
abbrev Cycle (α β : Type*)
```

`Cslib.RelationAlgebra.IntegralAtom.Cycle.left` (definition, [line 73](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/IntegralAtomStructure.lean#L73))

> The left cycle transformation: `t ≤ r * u` implies `u ≤ conv r * t`

```lean
def Cycle.left : Cycle α β → Cycle α β
```

`Cslib.RelationAlgebra.IntegralAtom.Cycle.right` (definition, [line 77](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/IntegralAtomStructure.lean#L77))

> The right cycle transformation: `t ≤ r * u` implies `r ≤ t * conv u`

```lean
def Cycle.right : Cycle α β → Cycle α β
```

`Cslib.RelationAlgebra.IntegralAtom.Cycle.IsDiversity` (abbreviation, [line 81](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/IntegralAtomStructure.lean#L81))

> A cycle without identity.

```lean
abbrev Cycle.IsDiversity : Cycle α β → Prop
```

`Cslib.RelationAlgebra.IntegralAtom.CycleClosure` (inductive type, [line 85](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/IntegralAtomStructure.lean#L85))

> The union of the Peircean orbits of the generators and all identity cycles.

```lean
inductive CycleClosure (g : Set (Cycle α β)) : Cycle α β → Prop
  | of {c : Cycle α β} : c ∈ g → CycleClosure g c
  | id (x : IntegralAtom α β) : CycleClosure g (x, one, x)
  | left {c : Cycle α β} : CycleClosure g c → CycleClosure g c.left
  | right {c : Cycle α β} : CycleClosure g c → CycleClosure g c.right
```

`Cslib.RelationAlgebra.IntegralAtom.conv_one` (theorem, [line 92](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/IntegralAtomStructure.lean#L92))

```lean
theorem conv_one : conv (one : IntegralAtom α β) = one
```

`Cslib.RelationAlgebra.IntegralAtom.conv_symm` (theorem, [line 95](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/IntegralAtomStructure.lean#L95))

```lean
theorem conv_symm (a : α) : conv (symm a : IntegralAtom α β) = symm a
```

`Cslib.RelationAlgebra.IntegralAtom.conv_nsymm` (theorem, [line 98](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/IntegralAtomStructure.lean#L98))

```lean
theorem conv_nsymm (b : β) (d : Bool) : conv (nsymm b d : IntegralAtom α β) = nsymm b !d
```

`Cslib.RelationAlgebra.IntegralAtom.conv_conv` (theorem, [line 101](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/IntegralAtomStructure.lean#L101))

```lean
theorem conv_conv (x : IntegralAtom α β) : conv (conv x) = x
```

`Cslib.RelationAlgebra.IntegralAtom.CycleClosure.id_cycle_left` (theorem, [line 110](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/IntegralAtomStructure.lean#L110))

```lean
theorem CycleClosure.id_cycle_left {g : Set (Cycle α β)} (hg : ∀ c ∈ g, c.IsDiversity)
    {u t : IntegralAtom α β} (h : CycleClosure g (one, u, t)) : t = u
```

`Cslib.RelationAlgebra.IntegralAtom.CycleClosure.id_cycle_right` (theorem, [line 114](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/IntegralAtomStructure.lean#L114))

```lean
theorem CycleClosure.id_cycle_right {g : Set (Cycle α β)} (hg : ∀ c ∈ g, c.IsDiversity)
    {r t : IntegralAtom α β} (h : CycleClosure g (r, one, t)) : t = r
```

`Cslib.RelationAlgebra.IntegralAtom.CycleClosure.id_cycle_conv` (theorem, [line 118](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/IntegralAtomStructure.lean#L118))

```lean
theorem CycleClosure.id_cycle_conv {g : Set (Cycle α β)} (hg : ∀ c ∈ g, c.IsDiversity)
    {r u : IntegralAtom α β} (h : CycleClosure g (r, u, one)) : u = conv r
```

`Cslib.RelationAlgebra.IntegralAtom.cycleClosure_one_iff` (theorem, [line 122](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/IntegralAtomStructure.lean#L122))

```lean
theorem cycleClosure_one_iff {g : Set (Cycle α β)} (hg : ∀ c ∈ g, c.IsDiversity)
    {r p : IntegralAtom α β} : CycleClosure g (r, one, p) ↔ p = r
```

`Cslib.RelationAlgebra.IntegralAtom.ofCycles` (definition, [line 127](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/IntegralAtomStructure.lean#L127))

> Construct an `AtomStructure` from diversity cycle generators.

```lean
def ofCycles (g : Set (Cycle α β)) : AtomStructure (IntegralAtom α β)
```

`Cslib.RelationAlgebra.IntegralAtom.ofCycles_conv` (theorem, [line 133](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/IntegralAtomStructure.lean#L133))

```lean
theorem ofCycles_conv (g : Set (Cycle α β)) (x : IntegralAtom α β) :
    (ofCycles g).conv x = conv x
```

`Cslib.RelationAlgebra.IntegralAtom.mem_ofCycles_id` (theorem, [line 137](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/IntegralAtomStructure.lean#L137))

```lean
theorem mem_ofCycles_id {g : Set (Cycle α β)} {x : IntegralAtom α β} :
    x ∈ (ofCycles g).id ↔ x = one
```

`Cslib.RelationAlgebra.IntegralAtom.mem_ofCycles_cycles` (theorem, [line 141](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/IntegralAtomStructure.lean#L141))

```lean
theorem mem_ofCycles_cycles {g : Set (Cycle α β)} {c : Cycle α β} :
    c ∈ (ofCycles g).cycles ↔ CycleClosure g c
```

`Cslib.RelationAlgebra.IntegralAtom.lawfulAtomStructure_ofCycles` (theorem, [line 144](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/IntegralAtomStructure.lean#L144))

```lean
theorem lawfulAtomStructure_ofCycles (g : Set (Cycle α β))
    (hassoc : ∀ {r q p u t}, CycleClosure g (r, q, p) → CycleClosure g (u, t, q) →
      ∃ q', CycleClosure g (q', t, p) ∧ CycleClosure g (r, u, q'))
    (hg : ∀ c ∈ g, c.IsDiversity) :
    LawfulAtomStructure (ofCycles g)
```

`Cslib.RelationAlgebra.IntegralAtom.isIntegral_ofCycles` (theorem, [line 156](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/IntegralAtomStructure.lean#L156))

> The complex algebra constructed from diversity cycles is integral.

```lean
theorem isIntegral_ofCycles (g : Set (Cycle α β)) [LawfulAtomStructure (ofCycles g)] :
    IsIntegral (ComplexAlgebra (ofCycles g))
```

`Cslib.RelationAlgebra.IntegralAtom.preimage_singleton_symmetricDiversityAtoms` (theorem, [line 160](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/IntegralAtomStructure.lean#L160))

```lean
theorem preimage_singleton_symmetricDiversityAtoms (g : Set (Cycle α β))
    [LawfulAtomStructure (ofCycles g)] :
    singleton ⁻¹' symmetricDiversityAtoms (ComplexAlgebra (ofCycles g)) = Set.range symm
```

`Cslib.RelationAlgebra.IntegralAtom.preimage_singleton_nonsymmetricDiversityAtoms` (theorem, [line 166](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/IntegralAtomStructure.lean#L166))

```lean
theorem preimage_singleton_nonsymmetricDiversityAtoms (g : Set (Cycle α β))
    [LawfulAtomStructure (ofCycles g)] :
    singleton ⁻¹' nonsymmetricDiversityAtoms (ComplexAlgebra (ofCycles g)) =
      Set.range (Function.uncurry nsymm)
```

`Cslib.RelationAlgebra.IntegralAtom.ncard_symmetricDiversityAtoms_ofCycles` (theorem, [line 173](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/IntegralAtomStructure.lean#L173))

```lean
theorem ncard_symmetricDiversityAtoms_ofCycles (g : Set (Cycle α β))
    [LawfulAtomStructure (ofCycles g)] :
    (symmetricDiversityAtoms (ComplexAlgebra (ofCycles g))).ncard = Nat.card α
```

`Cslib.RelationAlgebra.IntegralAtom.ncard_nonsymmetricDiversityAtoms_ofCycles` (theorem, [line 180](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/IntegralAtomStructure.lean#L180))

```lean
theorem ncard_nonsymmetricDiversityAtoms_ofCycles (g : Set (Cycle α β))
    [LawfulAtomStructure (ofCycles g)] :
    (nonsymmetricDiversityAtoms (ComplexAlgebra (ofCycles g))).ncard = 2 * Nat.card β
```

`Cslib.RelationAlgebra.IntegralAtom.setoid` (instance, [line 191](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/IntegralAtomStructure.lean#L191))

```lean
instance setoid (α β : Type*) :
    Setoid {g : Set (Cycle α β) // LawfulAtomStructure (ofCycles g)}
```

`Cslib.RelationAlgebra.IntegralAtom.IsoClass.ofSymmNsymm` (abbreviation, [line 208](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/IntegralAtomStructure.lean#L208))

> The set of isomorphism classes with `s` symmetric diversity atoms and `n` pairs of nonsymmetric
> atoms. This is an abbrev for the convenience of matching the usual convention without making proofs
> more complicated.

```lean
abbrev ofSymmNsymm (s n : ℕ) : Type
```

`Cslib.RelationAlgebra.IntegralAtom.IsoClass.ofAtoms` (abbreviation, [line 211](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/IntegralAtomStructure.lean#L211))

> The set of isomorphism classes with `k` atoms.

```lean
abbrev ofAtoms (k : ℕ) : Type
```

`Cslib.RelationAlgebra.IntegralAtom.IsoClass.isEmpty_ofAtoms_zero` (theorem, [line 213](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/IntegralAtomStructure.lean#L213))

```lean
theorem isEmpty_ofAtoms_zero : IsEmpty (ofAtoms 0)
```

`Cslib.RelationAlgebra.IntegralAtom.IsoClass.card_ofAtoms_succ_eq_sum_ofSymmNsymm` (theorem, [line 216](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/IntegralAtomStructure.lean#L216))

```lean
theorem card_ofAtoms_succ_eq_sum_ofSymmNsymm (k : ℕ) :
    Nat.card (ofAtoms (k + 1)) =
      ∑ n ∈ Finset.range (k / 2 + 1), Nat.card (ofSymmNsymm (k - 2 * n) n)
```

> ### Counts of isomorphism classes
>
> The following statements are all of the known counts of isomorphism classes of finite integral
> relation algebras, by symmetric and nonsymmetric atoms as well as overall.
>
> They will certainly be too computationally expensive to prove here, but we
> provide their statements as a reference. Proofs of the `ofAtoms` statements can start with
> `simp [card_ofAtoms_succ_eq_sum_ofSymmNsymm, Finset.sum_range_succ]` and then use each of
> the `ofSymmNsymm` results.

## Depends on

- [Atom structures](atomstructure.md)

## Sources

- [Cslib/Foundations/RelationAlgebra/IntegralAtomStructure.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/IntegralAtomStructure.lean)
- [Declaration ledger](../../../../sources/cslib/Cslib.Foundations.RelationAlgebra.IntegralAtomStructure.json)
