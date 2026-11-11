---
declaration: section
origin: cited
lean: IsDedekindDomain.HeightOneSpectrum.finite_residueField, IsDedekindDomain.HeightOneSpectrum.isCompact_adicCompletionIntegers, NumberField.localIntegralUnitSubgroup, NumberField.FiniteIdeleGroup, NumberField.FiniteIdeleGroup.isOpen_localIntegralUnitSubgroup, NumberField.InfiniteIdeleGroup, NumberField.TopologicalIdeleGroup, NumberField.TopologicalIdeleGroup.infinitePrincipalEmbedding
statement: formalized
proof: formalized
---

# Adeles and ideles

25 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/adeles-and-ideles/index.html).

## Finite residue field of a completed number ring

Let $K$ be a number field and $v$ a
nonzero prime ideal of its ring of integers $\mathcal{O}_K$. The residue field of the ring of
integers $\mathcal{O}_v$ of the $v$-adic completion $K_v$ of $K$ is finite.

Formalized by `IsDedekindDomain.HeightOneSpectrum.finite_residueField`, a theorem declared in [MathlibExt/NumberTheory/NumberField/AdeleLocallyCompact.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/AdeleLocallyCompact.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/adeles-and-ideles/index.html#finite-residue-field).

## Compactness of the completed ring of integers

Let $K$ be a number field and $v$ a
nonzero prime ideal of its ring of integers $\mathcal{O}_K$. The ring of integers $\mathcal{O}_v$
of the $v$-adic completion $K_v$ of $K$ is a compact subset of $K_v$.

Formalized by `IsDedekindDomain.HeightOneSpectrum.isCompact_adicCompletionIntegers`, a theorem declared in [MathlibExt/NumberTheory/NumberField/AdeleLocallyCompact.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/AdeleLocallyCompact.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/adeles-and-ideles/index.html#is-compact-adic-completion-integers).

## Local integral unit subgroup

Let $R$ be a Dedekind domain with fraction field $K$, let $v$
be a height-one prime of $R$, and let $\mathcal{O}_v$ be the ring of integers of the $v$-adic
completion $K_v$ of $K$. The local integral unit subgroup is the subgroup $\mathcal{O}_v^\times$
of $K_v^\times$, consisting of the units $u$ of $K_v$ with $u \in \mathcal{O}_v$ and
$u^{-1} \in \mathcal{O}_v$.

Formalized by `NumberField.localIntegralUnitSubgroup`, an abbreviation declared in [MathlibExt/NumberTheory/NumberField/Idele.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/Idele.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/adeles-and-ideles/index.html#local-integral-unit-subgroup).

## Finite idele group

Let $R$ be a Dedekind domain with fraction field $K$. For each
height-one prime $v$ of $R$, let $K_v$ be the $v$-adic completion of $K$ and $\mathcal{O}_v$ its
ring of integers. The finite idele group is the restricted product of the unit groups $K_v^\times$
over all height-one primes $v$ of $R$ with respect to the subgroups $\mathcal{O}_v^\times$: the
families $(x_v)_v$ with $x_v \in K_v^\times$ for every $v$ and $x_v \in \mathcal{O}_v^\times$ for
all but finitely many $v$, with componentwise multiplication and the restricted-product topology.

Formalized by `NumberField.FiniteIdeleGroup`, a definition declared in [MathlibExt/NumberTheory/NumberField/Idele.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/Idele.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/adeles-and-ideles/index.html#finite-idele-group).

## The local integral units are open

Let $R$ be a Dedekind domain with fraction field $K$,
let $v$ be a height-one prime of $R$, and let $\mathcal{O}_v$ be the ring of integers of the
$v$-adic completion $K_v$ of $K$. Then $\mathcal{O}_v^\times$ is an open subset of the unit group
$K_v^\times$.

Formalized by `NumberField.FiniteIdeleGroup.isOpen_localIntegralUnitSubgroup`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Idele.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/Idele.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/adeles-and-ideles/index.html#is-open-local-integral-unit-subgroup).

## Infinite idele group

For a field $K$, the infinite idele group is the product
$\prod_v K_v^\times$ of the unit groups of the completions $K_v$ of $K$ over all infinite places
$v$ of $K$, with componentwise multiplication and the product topology.

Formalized by `NumberField.InfiniteIdeleGroup`, a definition declared in [MathlibExt/NumberTheory/NumberField/Idele.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/Idele.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/adeles-and-ideles/index.html#infinite-idele-group).

## Topological idele group

Let $R$ be a Dedekind domain with fraction field $K$. The
topological idele group is the product $\mathbb{I}_{K,\infty} \times \mathbb{I}_{K,f}$ of the
infinite idele group $\mathbb{I}_{K,\infty} = \prod_w K_w^\times$, the product of the unit groups
of the completions of $K$ at its infinite places $w$, and the finite idele group
$\mathbb{I}_{K,f}$, the restricted product of the unit groups $K_v^\times$ of the completions at
the height-one primes $v$ of $R$ with respect to the integral unit groups $\mathcal{O}_v^\times$.
It carries the componentwise group structure and the product of the product topology on
$\mathbb{I}_{K,\infty}$ and the restricted-product topology on $\mathbb{I}_{K,f}$.

As a group it is isomorphic to the unit group of the adele ring of $K$, but its topology differs
from the subspace topology on those units.

Formalized by `NumberField.TopologicalIdeleGroup`, a definition declared in [MathlibExt/NumberTheory/NumberField/Idele.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/Idele.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/adeles-and-ideles/index.html#topological-idele-group).

## Diagonal map into the infinite ideles

For a field $K$, this is the group homomorphism
from $K^\times$ to the infinite idele group of $K$ that sends $x$ to the family of its images in the
completions $K_v$ of $K$, one for each infinite place $v$ of $K$.

Formalized by `NumberField.TopologicalIdeleGroup.infinitePrincipalEmbedding`, a definition declared in [MathlibExt/NumberTheory/NumberField/Idele.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/Idele.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/adeles-and-ideles/index.html#infinite-principal-embedding).

## Diagonal map into the finite ideles

Let $R$ be a Dedekind domain with fraction field $K$.
This is the group homomorphism from $K^\times$ to the finite idele group of $R$ and $K$ that sends
$x$ to the family of its images in the $v$-adic completions $K_v$ of $K$, one for each height-one
prime $v$ of $R$.

Formalized by `NumberField.TopologicalIdeleGroup.finitePrincipalEmbedding`, a definition declared in [MathlibExt/NumberTheory/NumberField/Idele.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/Idele.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/adeles-and-ideles/index.html#finite-principal-embedding).

## Diagonal map into the ideles

Let $R$ be a Dedekind domain with fraction field $K$. This
is the group homomorphism from $K^\times$ to the topological idele group of $R$ and $K$ whose
infinite component sends $x$ to its images in the completions of $K$ at all infinite places of
$K$, and whose finite component sends $x$ to its images in the $v$-adic completions $K_v$ of $K$
at all height-one primes $v$ of $R$.

Formalized by `NumberField.TopologicalIdeleGroup.principalEmbedding`, a definition declared in [MathlibExt/NumberTheory/NumberField/Idele.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/Idele.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/adeles-and-ideles/index.html#principal-embedding).

## Principal ideles

Let $R$ be a Dedekind domain with fraction field $K$. The subgroup of
principal ideles is the image of the diagonal homomorphism from $K^\times$ to the topological idele
group of $R$ and $K$, which sends $x$ to its images in the completions of $K$ at all infinite
places of $K$ and at all height-one primes of $R$.

Formalized by `NumberField.TopologicalIdeleGroup.principalIdeles`, a definition declared in [MathlibExt/NumberTheory/NumberField/Idele.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/Idele.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/adeles-and-ideles/index.html#principal-ideles).

## Ideles as units of the adele ring

Let $R$ be a Dedekind domain with fraction field $K$,
and let $\mathbb{A}_K$ be the adele ring of $K$ built from the infinite places of $K$ and the
height-one primes of $R$. For an infinite place $w$ of $K$ write $K_w$ for the completion of $K$
at $w$, and for a height-one prime $v$ of $R$ write $K_v$ for the $v$-adic completion of $K$.
This is the group isomorphism from the unit group $\mathbb{A}_K^\times$ to the topological idele
group that sends a unit adele $a$ to the idele whose component at each infinite place $w$ is the
component $a_w \in K_w^\times$ of $a$ and whose component at each height-one prime $v$ is the
component $a_v \in K_v^\times$ of $a$.

It is stated only as an isomorphism of groups: the topological idele group carries the
restricted-product topology, not the topology induced on the units of the adele ring.

Formalized by `NumberField.TopologicalIdeleGroup.unitsEquiv`, a definition declared in [MathlibExt/NumberTheory/NumberField/Idele.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/Idele.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/adeles-and-ideles/index.html#units-equiv).

## The diagonal map into the ideles is injective

Let $K$ be a number field and let $R$ be a
Dedekind domain with fraction field $K$. The diagonal homomorphism from $K^\times$ to the
topological idele group of $R$ and $K$, which sends $x$ to its images in the completions of $K$ at
all infinite places of $K$ and at all height-one primes of $R$, is injective.

Formalized by `NumberField.TopologicalIdeleGroup.principalEmbedding_injective`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Idele.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/Idele.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/adeles-and-ideles/index.html#principal-embedding-injective).

## Topological idele class group

Let $R$ be a Dedekind domain with fraction field $K$. The
topological idele class group is the quotient group of the topological idele group of $R$ and $K$
by its subgroup of principal ideles, the image of the diagonal homomorphism from $K^\times$.

Formalized by `NumberField.TopologicalIdeleClassGroup`, an abbreviation declared in [MathlibExt/NumberTheory/NumberField/Idele.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/Idele.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/adeles-and-ideles/index.html#topological-idele-class-group).

## Compactness of the local integral units

Let $K$ be a number field, let $v$ be a
height-one prime of its ring of integers $\mathcal{O}_K$, and let $\mathcal{O}_v$ be the ring of
integers of the $v$-adic completion $K_v$ of $K$. Then the local integral unit subgroup
$\mathcal{O}_v^\times$ is a compact subset of the unit group $K_v^\times$.

It is the unit group of the compact valuation subring $\mathcal{O}_v$.

Formalized by `NumberField.FiniteIdeleGroup.isCompact_localIntegralUnitSubgroup`, a theorem declared in [MathlibExt/NumberTheory/NumberField/IdeleLocallyCompact.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/IdeleLocallyCompact.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/adeles-and-ideles/index.html#is-compact-local-integral-unit-subgroup).

## Adelic norm

Let $K$ be a number field with ring of integers $\mathcal{O}_K$. For each
infinite place $w$ of $K$ let $K_w$ be the completion of $K$ at $w$, with the absolute value
$\|\cdot\|_w$ extending $w$, and let $m_w$ be $1$ if $w$ is real and $2$ if $w$ is complex. For
each height-one prime $v$ of $\mathcal{O}_K$ let $K_v$ be the $v$-adic completion of $K$, with
the normalized absolute value $\|\cdot\|_v$. The adelic norm is the monoid homomorphism from the
topological idele group of $K$ over the Dedekind domain $\mathcal{O}_K$ to the real numbers under
multiplication that sends an idele $a$, with components $a_w \in K_w^\times$ and
$a_v \in K_v^\times$, to $\bigl(\prod_w \|a_w\|_w^{m_w}\bigr) \cdot \prod_v \|a_v\|_v$, where the
product over $v$ is the product of its finitely many factors different from $1$.

Formalized by `NumberField.TopologicalIdeleGroup.adelicNorm`, a definition declared in [MathlibExt/NumberTheory/NumberField/IdeleNorm.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/IdeleNorm.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/adeles-and-ideles/index.html#adelic-norm).

## Formula for the adelic norm

Let $K$ be a number field. For every idele $a$ of $K$ (with
$R = \mathcal{O}_K$), the adelic norm of $a$ equals
$\bigl(\prod_w \|a_w\|_w^{m_w}\bigr) \cdot \prod_v \|a_v\|_v$, where $w$ runs over the infinite
places of $K$, $\|\cdot\|_w$ is the absolute value on the completion $K_w$ extending $w$, $m_w$ is
$1$ for a real place and $2$ for a complex place, $v$ runs over the height-one primes of
$\mathcal{O}_K$, $\|\cdot\|_v$ is the normalized absolute value on the completion $K_v$, and the
product over $v$ is the product of its finitely many factors different from $1$.

Formalized by `NumberField.TopologicalIdeleGroup.adelicNorm_apply`, a theorem declared in [MathlibExt/NumberTheory/NumberField/IdeleNorm.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/IdeleNorm.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/adeles-and-ideles/index.html#adelic-norm-apply).

## Norm-one ideles

Let $K$ be a number field. The norm-one ideles of $K$ form the kernel of
the adelic norm, the subgroup of the topological idele group of $K$ (with $R = \mathcal{O}_K$)
consisting of the ideles whose adelic norm is $1$.

Formalized by `NumberField.TopologicalIdeleGroup.normOneIdeles`, a definition declared in [MathlibExt/NumberTheory/NumberField/IdeleNorm.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/IdeleNorm.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/adeles-and-ideles/index.html#norm-one-ideles).

## Membership in the norm-one ideles

Let $K$ be a number field. An idele $a$ of $K$ (with
$R = \mathcal{O}_K$) lies in the subgroup of norm-one ideles if and only if its adelic norm
is $1$.

Formalized by `NumberField.TopologicalIdeleGroup.mem_normOneIdeles`, a theorem declared in [MathlibExt/NumberTheory/NumberField/IdeleNorm.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/IdeleNorm.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/adeles-and-ideles/index.html#mem-norm-one-ideles).

## Product formula for principal ideles

Let $K$ be a number field. For every
$x \in K^\times$, the principal idele of $x$ (its image under the diagonal embedding of $K^\times$
into the topological idele group, with $R = \mathcal{O}_K$) has adelic norm $1$.

Formalized by `NumberField.TopologicalIdeleGroup.adelicNorm_principalEmbedding`, a theorem declared in [MathlibExt/NumberTheory/NumberField/IdeleNorm.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/IdeleNorm.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/adeles-and-ideles/index.html#adelic-norm-principal-embedding).

## Principal ideles have norm one

Let $K$ be a number field. The subgroup of principal
ideles of $K$ (with $R = \mathcal{O}_K$) is contained in the subgroup of norm-one ideles; that
is, every principal idele has adelic norm $1$.

Formalized by `NumberField.TopologicalIdeleGroup.principalIdeles_le_normOneIdeles`, a theorem declared in [MathlibExt/NumberTheory/NumberField/IdeleNorm.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/IdeleNorm.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/adeles-and-ideles/index.html#principal-ideles-le-norm-one-ideles).

## Principal ideles of norm one

For a number field $K$, this is the subgroup of the group
$I_K^1$ of ideles of $K$ with adelic norm $1$ consisting of the principal ideles, that is, of the
elements of $I_K^1$ that are images of elements of $K^\times$ under the diagonal embedding.

Formalized by `NumberField.TopologicalIdeleGroup.normOnePrincipalIdeles`, a definition declared in [MathlibExt/NumberTheory/NumberField/NormOneIdeleClassGroup.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/NormOneIdeleClassGroup.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/adeles-and-ideles/index.html#norm-one-principal-ideles).

## Norm-one idele class group

For a number field $K$, the norm-one idele class group
$C_K^1 = I_K^1 / K^\times$ is the quotient of the group $I_K^1$ of ideles of $K$ with adelic norm
$1$ by its subgroup of principal ideles, the images of the elements of $K^\times$ under the
diagonal embedding.

Formalized by `NumberField.TopologicalIdeleGroup.NormOneIdeleClassGroup`, an abbreviation declared in [MathlibExt/NumberTheory/NumberField/NormOneIdeleClassGroup.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/NormOneIdeleClassGroup.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/adeles-and-ideles/index.html#norm-one-idele-class-group).

## Principal ideles are trivial in the norm-one idele class group

Let $K$ be a number field.
For every $x \in K^\times$, the principal idele of $x$, viewed as an element of the group $I_K^1$
of ideles of $K$ with adelic norm $1$, has trivial class in the norm-one idele class group
$C_K^1 = I_K^1 / K^\times$.

Formalized by `NumberField.TopologicalIdeleGroup.normOne_mk_principalEmbedding`, a theorem declared in [MathlibExt/NumberTheory/NumberField/NormOneIdeleClassGroup.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/NormOneIdeleClassGroup.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/adeles-and-ideles/index.html#norm-one-mk-principal-embedding).

## The principal ideles are discrete

For a number field $K$, the subgroup of principal
ideles is discrete in the idele group of $K$, where the idele group carries the product of the
product topology at the infinite places and the restricted-product topology at the finite
places.

Formalized by `NumberField.TopologicalIdeleGroup.principalIdeles_discrete`, a theorem declared in [MathlibExt/NumberTheory/NumberField/PrincipalIdele.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/PrincipalIdele.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/adeles-and-ideles/index.html#principal-ideles-discrete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Adeles and ideles](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/adeles-and-ideles/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/adeles-and-ideles)
