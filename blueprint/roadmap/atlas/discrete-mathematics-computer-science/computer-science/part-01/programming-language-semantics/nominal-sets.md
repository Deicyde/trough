---
declaration: section
origin: cited
lean: Cslib.Nominal.finPermSubgroup, Cslib.Nominal.FinPerm, Cslib.Nominal.swap, Cslib.Nominal.swap_smul, Cslib.Nominal.swap_mul_self, Cslib.Nominal.swap_inv, Cslib.Nominal.swap_self, Cslib.Nominal.swap_comm
statement: formalized
proof: formalized
---

# Nominal sets

46 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html).

## Subgroup of finitely supported permutations of atoms

The subgroup of finitely supported permutations of `Atom`: permutations
that fix all atoms outside some finite set.

Formalized by `Cslib.Nominal.finPermSubgroup`, a definition declared in [CSLibExt/Foundations/Nominal/Basic.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Basic.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#fin-perm-subgroup).

## Group of finitely supported permutations

The group of finitely supported permutations of `Atom`.

Formalized by `Cslib.Nominal.FinPerm`, an abbreviation declared in [CSLibExt/Foundations/Nominal/Basic.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Basic.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#fin-perm).

## Transposition of two atoms

The transposition of two atoms, as a finite permutation.

Formalized by `Cslib.Nominal.swap`, a definition declared in [CSLibExt/Foundations/Nominal/Basic.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Basic.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#swap).

## Action of a transposition

Applying a transposition is applying the underlying `Equiv.swap`.

Formalized by `Cslib.Nominal.swap_smul`, a theorem declared in [CSLibExt/Foundations/Nominal/Basic.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Basic.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#swap-smul).

## A transposition squares to the identity

A transposition is an involution, stated for the `FinPerm` group.

Formalized by `Cslib.Nominal.swap_mul_self`, a theorem declared in [CSLibExt/Foundations/Nominal/Basic.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Basic.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#swap-mul-self).

## A transposition is its own inverse

A transposition is its own inverse.

Formalized by `Cslib.Nominal.swap_inv`, a theorem declared in [CSLibExt/Foundations/Nominal/Basic.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Basic.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#swap-inv).

## Transposition of an atom with itself is the identity

A transposition of an atom with itself is the identity.

Formalized by `Cslib.Nominal.swap_self`, a theorem declared in [CSLibExt/Foundations/Nominal/Basic.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Basic.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#swap-self).

## Symmetry of transpositions

Transpositions are symmetric.

Formalized by `Cslib.Nominal.swap_comm`, a theorem declared in [CSLibExt/Foundations/Nominal/Basic.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Basic.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#swap-comm).

## Conjugation of a transposition

Conjugation of a transposition: `σ * swap b c * σ⁻¹ = swap (σ b) (σ c)`.

Formalized by `Cslib.Nominal.swap_conj`, a theorem declared in [CSLibExt/Foundations/Nominal/Basic.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Basic.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#swap-conj).

## Transposition fixes atoms other than the swapped pair

A transposition fixes every atom distinct from its two swapped atoms.

Formalized by `Cslib.Nominal.swap_smul_of_ne_of_ne`, a theorem declared in [CSLibExt/Foundations/Nominal/Basic.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Basic.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#swap-smul-of-ne-of-ne).

## Supporting set of atoms for an element

`S` supports `x` when every finite permutation fixing `S` pointwise fixes `x`.

Formalized by `Cslib.Nominal.Supports`, a definition declared in [CSLibExt/Foundations/Nominal/Basic.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Basic.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#supports).

## Enlarging a support

A support can be enlarged: fixing a larger set pointwise is a stronger
hypothesis.

Formalized by `Cslib.Nominal.Supports.mono`, a theorem declared in [CSLibExt/Foundations/Nominal/Basic.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Basic.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#mono).

## Nominal set

A type with an action of finite permutations in which every element has a
finite support: a *nominal set*.

Formalized by `Cslib.Nominal.NominalSet`, a class declared in [CSLibExt/Foundations/Nominal/Basic.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Basic.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#nominal-set).

## A pair is supported by the union of its components' supports

A pair is supported by the union of supports of its components.

Formalized by `Cslib.Nominal.Supports.prod`, a theorem declared in [CSLibExt/Foundations/Nominal/Basic.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Basic.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#prod).

## Freshness of an atom for an element

`a` is *fresh* for `x`, written `a # x` in the nominal literature, when
some finite support of `x` does not contain `a`.

Formalized by `Cslib.Nominal.Fresh`, a definition declared in [CSLibExt/Foundations/Nominal/Basic.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Basic.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#fresh).

## Existence of fresh atoms

Every element has a fresh atom: choose one outside any of its supports.

Formalized by `Cslib.Nominal.exists_fresh`, a theorem declared in [CSLibExt/Foundations/Nominal/Basic.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Basic.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#exists-fresh).

## Transposition of atoms outside a support fixes the element

A transposition of two atoms both outside a support of `x` fixes `x`.

Formalized by `Cslib.Nominal.swap_smul_of_supports_not_mem`, a theorem declared in [CSLibExt/Foundations/Nominal/Basic.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Basic.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#swap-smul-of-supports-not-mem).

## Swapping two fresh atoms fixes the element

Swapping two fresh atoms fixes `x`. The proof uses a third atom `c` fresh
for both witnessing supports, and the conjugation identity
`swap a b = swap a c * swap b c * swap a c`.

Formalized by `Cslib.Nominal.swap_smul_of_fresh_fresh`, a theorem declared in [CSLibExt/Foundations/Nominal/Basic.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Basic.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#swap-smul-of-fresh-fresh).

## Permutations moving only fresh atoms fix the element

A permutation that fixes every atom outside a finite set `F` of fresh
atoms fixes `x`, by induction on `F`. If `π a = a` we apply the induction
hypothesis to `π`; otherwise we factor `π = swap a b * π'` with `b = π a`,
where `π'` fixes `a` and has support inside `F \ {a}`, and `swap a b` fixes
`x` since `a` and `b` are fresh.

Formalized by `Cslib.Nominal.smul_eq_of_fresh`, a theorem declared in [CSLibExt/Foundations/Nominal/Basic.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Basic.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#smul-eq-of-fresh).

## Intersection of two supports is a support

The intersection of two supports is a support: a permutation fixing the
intersection fixes `x`, since every atom it can move (outside some finite
support of the permutation, and outside the intersection) is fresh for `x`.

Formalized by `Cslib.Nominal.Supports.inter`, a theorem declared in [CSLibExt/Foundations/Nominal/Basic.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Basic.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#inter).

## Permutation image of a support

A permutation moves a support of `x` to a support of `π • x`.

Formalized by `Cslib.Nominal.Supports.image`, a theorem declared in [CSLibExt/Foundations/Nominal/Basic.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Basic.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#image).

## Existence of a least finite support

A least finite support exists: among the supports of `x`, one is
contained in every support. The proof is by strong induction on a chosen
support `S₀`: either every element of `S₀` lies in every support (so `S₀`
itself is least), or some `a ∈ S₀` is missing from a support `Sₐ`, and the
induction hypothesis applies to the strictly smaller support `Sₐ ∩ S₀`.

Formalized by `Cslib.Nominal.exists_least_support`, a theorem declared in [CSLibExt/Foundations/Nominal/Basic.lean, line 351](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Basic.lean#L351). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#exists-least-support).

## Least finite support of an element

The *least* finite support of `x`: a support contained in every support
of `x`.

Formalized by `Cslib.Nominal.supp`, a definition declared in [CSLibExt/Foundations/Nominal/Basic.lean, line 373](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Basic.lean#L373). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#supp).

## Least support is a support

The least support is a support.

Formalized by `Cslib.Nominal.supp_supports`, a theorem declared in [CSLibExt/Foundations/Nominal/Basic.lean, line 379](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Basic.lean#L379). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#supp-supports).

## Minimality of the least support

The least support is contained in every support: minimality.

Formalized by `Cslib.Nominal.supp_subset`, a theorem declared in [CSLibExt/Foundations/Nominal/Basic.lean, line 385](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Basic.lean#L385). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#supp-subset).

## Membership in the least support

Membership in the least support: `a ∈ supp (Atom := Atom) x` iff `a` lies in every
support of `x`.

Formalized by `Cslib.Nominal.mem_supp_iff`, a theorem declared in [CSLibExt/Foundations/Nominal/Basic.lean, line 392](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Basic.lean#L392). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#mem-supp-iff).

## Freshness is non-membership in the least support

Freshness is exactly non-membership in the least support.

Formalized by `Cslib.Nominal.fresh_iff_not_mem_supp`, a theorem declared in [CSLibExt/Foundations/Nominal/Basic.lean, line 401](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Basic.lean#L401). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#fresh-iff-not-mem-supp).

## Equivariance of the least support

Support is equivariant: permuting `x` permutes its support.

Formalized by `Cslib.Nominal.supp_smul`, a theorem declared in [CSLibExt/Foundations/Nominal/Basic.lean, line 415](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Basic.lean#L415). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#supp-smul).

## Support of an atom

The support of an atom is its singleton.

Formalized by `Cslib.Nominal.supp_atom`, a theorem declared in [CSLibExt/Foundations/Nominal/Basic.lean, line 437](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Basic.lean#L437). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#supp-atom).

## Permutations agreeing on the support act equally

Two permutations that agree on the support of `x` act equally on `x`:
their ratio fixes the support pointwise, hence fixes `x`.

Formalized by `Cslib.Nominal.smul_eq_of_agree_on_supp`, a theorem declared in [CSLibExt/Foundations/Nominal/Basic.lean, line 460](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Basic.lean#L460). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#smul-eq-of-agree-on-supp).

## Equivariant elements of a nominal set

An element fixed by every permutation has the empty set as a support.

Formalized by `Cslib.Nominal.IsEquivariant`, a definition declared in [CSLibExt/Foundations/Nominal/Basic.lean, line 472](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Basic.lean#L472). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#is-equivariant).

## Equivariant elements are supported by the empty set

An equivariant element is supported by the empty set.

Formalized by `Cslib.Nominal.supports_empty_of_equivariant`, a theorem declared in [CSLibExt/Foundations/Nominal/Basic.lean, line 476](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Basic.lean#L476). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#supports-empty-of-equivariant).

## Equivariant elements have empty support

An equivariant element has empty support.

Formalized by `Cslib.Nominal.supp_eq_empty_of_equivariant`, a theorem declared in [CSLibExt/Foundations/Nominal/Basic.lean, line 482](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Basic.lean#L482). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#supp-eq-empty-of-equivariant).

## α-equivalence relation on atom–element pairs

**α-equivalence relation on atom–element pairs.** α-equivalence: equal pairs, or a renaming of the bound atom by a fresh
transposition.

Formalized by `Cslib.Nominal.AbsRel`, a definition declared in [CSLibExt/Foundations/Nominal/Abstraction.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Abstraction.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#abs-rel).

## Reflexivity of α-equivalence

**Reflexivity of α-equivalence.** α-equivalence is reflexive.

Formalized by `Cslib.Nominal.absRel_refl`, a theorem declared in [CSLibExt/Foundations/Nominal/Abstraction.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Abstraction.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#abs-rel-refl).

## Symmetry of α-equivalence

**Symmetry of α-equivalence.** α-equivalence is symmetric. Symmetry uses equivariance of support
(`supp_smul`).

Formalized by `Cslib.Nominal.absRel_symm`, a theorem declared in [CSLibExt/Foundations/Nominal/Abstraction.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Abstraction.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#abs-rel-symm).

## Transitivity of α-equivalence

**Transitivity of α-equivalence.** α-equivalence is transitive. Transitivity uses the fact that two
permutations agreeing on `supp y` act equally on `y`
(`smul_eq_of_agree_on_supp`).

Formalized by `Cslib.Nominal.absRel_trans`, a theorem declared in [CSLibExt/Foundations/Nominal/Abstraction.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Abstraction.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#abs-rel-trans).

## Setoid of α-equivalence

The setoid of α-equivalence.

Formalized by `Cslib.Nominal.absSetoid`, a definition declared in [CSLibExt/Foundations/Nominal/Abstraction.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Abstraction.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#abs-setoid).

## Atom abstraction of a nominal set

Atom abstraction: `[a]x`, the quotient of `Atom × X` by α-equivalence.

Formalized by `Cslib.Nominal.Abs`, a definition declared in [CSLibExt/Foundations/Nominal/Abstraction.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Abstraction.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#abs).

## Abstraction of an element at a bound atom

The abstraction `[a]x`.

Formalized by `Cslib.Nominal.abs`, a definition declared in [CSLibExt/Foundations/Nominal/Abstraction.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Abstraction.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#abs-2).

## Equality of abstractions is α-equivalence

Equality of abstractions is α-equivalence.

Formalized by `Cslib.Nominal.abs_eq_iff`, a theorem declared in [CSLibExt/Foundations/Nominal/Abstraction.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Abstraction.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#abs-eq-iff).

## Abstractions with the same bound atom have equal bodies

An abstraction with the same bound atom determines its body.

Formalized by `Cslib.Nominal.abs_eq_of_same_atom`, a theorem declared in [CSLibExt/Foundations/Nominal/Abstraction.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Abstraction.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#abs-eq-of-same-atom).

## Permutation action on abstractions

The action of a permutation on abstractions, applied to a representative.

Formalized by `Cslib.Nominal.absSmul`, a definition declared in [CSLibExt/Foundations/Nominal/Abstraction.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Abstraction.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#abs-smul).

## Permutation action on abstractions computed on representatives

A permutation applied to an abstraction, on representatives.

Formalized by `Cslib.Nominal.smul_abs`, a theorem declared in [CSLibExt/Foundations/Nominal/Abstraction.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Abstraction.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#smul-abs).

## Abstractions are supported by the body's support minus the atom

The action of a permutation on an abstraction fixes it when the
permutation fixes `supp x \ {a}` pointwise.

Formalized by `Cslib.Nominal.supports_erase_abs`, a theorem declared in [CSLibExt/Foundations/Nominal/Abstraction.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Abstraction.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#supports-erase-abs).

## Support of an atom abstraction

The support of an abstraction is the body's support minus the bound atom.

Formalized by `Cslib.Nominal.supp_abs`, a theorem declared in [CSLibExt/Foundations/Nominal/Abstraction.lean, line 324](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Nominal/Abstraction.lean#L324). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html#supp-abs).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Nominal sets](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/nominal-sets/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/programming-language-semantics/nominal-sets)
