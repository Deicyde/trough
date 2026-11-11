---
declaration: section
origin: cited
lean: MetaMathlibExt.rackAut, MetaMathlibExt.VirtualRackIso, MetaMathlibExt.virtualRackClassCount, MetaMathlibExt.dihedralAffinePerm, MetaMathlibExt.virtualRackIso_refl, MetaMathlibExt.dihedralAffinePerm_mem_rackAut, MetaMathlibExt.zmodUnitsMulAut, MetaMathlibExt.cyclicHolomorph
statement: formalized
---

# Virtual racks and quandles

15 results, 9 proved and 6 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/virtual-racks-and-quandles/index.html).

## Automorphism group of a rack

For a rack $R$ with operation $\triangleleft$, the
automorphism group $\operatorname{Aut} R$ is the subgroup of the group of permutations of $R$
consisting of the permutations $f$ with $f(x \triangleleft y) = f(x) \triangleleft f(y)$ for all
$x, y \in R$.

Here $x \triangleleft y$ is the paper's $s_x(y)$.

## Sources

- Lực Ta, *Enumeration of Virtual Quandles Up to Isomorphism*, Journal of Integer Sequences 28 (2025), Article 25.8.4, Section 2.2 (rack homomorphisms and `Aut R`).

Formalized by `MetaMathlibExt.rackAut`, a definition declared in [WantedExt/Algebra/VirtualQuandleWanted.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/VirtualQuandleWanted.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/virtual-racks-and-quandles/index.html#rack-aut).

## Isomorphism of virtual racks

Write $x \triangleleft y$ for the operation of a rack. A
virtual rack $(R, f)$ is a rack $R$ together with a rack automorphism $f$ of $R$, its virtual
structure. Let $R_1$ and $R_2$ be racks and let $f_1$ and $f_2$ be permutations of $R_1$ and
$R_2$. Then $(R_1, f_1)$ and $(R_2, f_2)$ are isomorphic when there is a bijection
$\psi \colon R_1 \to R_2$ such that $\psi(x \triangleleft y) = \psi(x) \triangleleft \psi(y)$
for all $x, y \in R_1$ and $\psi(f_1(x)) = f_2(\psi(x))$ for all $x \in R_1$.

The definition does not require $f_1$ and $f_2$ to be rack automorphisms; for virtual racks it
is the usual notion of isomorphism.

## Sources

- Lực Ta, *Enumeration of Virtual Quandles Up to Isomorphism*, Journal of Integer Sequences 28 (2025), Article 25.8.4, Section 2.2 (virtual rack isomorphisms).

Formalized by `MetaMathlibExt.VirtualRackIso`, a definition declared in [WantedExt/Algebra/VirtualQuandleWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/VirtualQuandleWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/virtual-racks-and-quandles/index.html#virtual-rack-iso).

## Number of isomorphism classes of virtual racks on a rack

For a rack $R$, let
$\operatorname{Aut} R$ be its group of rack automorphisms; a virtual structure on $R$ is an
element $f \in \operatorname{Aut} R$, and $(R, f)$ is the corresponding virtual rack. The number
$v(R)$ is the number of classes of virtual structures on $R$, where $f, g \in \operatorname{Aut} R$
are identified when the virtual racks $(R, f)$ and $(R, g)$ are isomorphic; that is, the number
of isomorphism classes of virtual racks with underlying rack $R$. It is $0$ when there are
infinitely many classes.

Every virtual rack whose underlying rack is isomorphic to $R$ is isomorphic to one of the form
$(R, f)$.

## Sources

- Lực Ta, *Enumeration of Virtual Quandles Up to Isomorphism*, Journal of Integer Sequences 28 (2025), Article 25.8.4, Section 3.2.2 (the invariant `v(R)`).

Formalized by `MetaMathlibExt.virtualRackClassCount`, a definition declared in [WantedExt/Algebra/VirtualQuandleWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/VirtualQuandleWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/virtual-racks-and-quandles/index.html#virtual-rack-class-count).

## Affine permutations of the dihedral quandle

For a natural number $n$, an element
$a \in \mathbb{Z}/n\mathbb{Z}$ and a unit $u \in (\mathbb{Z}/n\mathbb{Z})^\times$, $T_{a,u}$ is the
affine map $x \mapsto a + u x$ of $\mathbb{Z}/n\mathbb{Z}$, viewed as a permutation of the
dihedral quandle $R_n$ (the set $\mathbb{Z}/n\mathbb{Z}$ with $x \triangleleft y = 2x - y$).

## Sources

- Lực Ta, *Enumeration of Virtual Quandles Up to Isomorphism*, Journal of Integer Sequences 28 (2025), Article 25.8.4, Section 2.2 (virtual structures on the dihedral quandle).

Formalized by `MetaMathlibExt.dihedralAffinePerm`, a definition declared in [WantedExt/Algebra/VirtualQuandleWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/VirtualQuandleWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/virtual-racks-and-quandles/index.html#dihedral-affine-perm).

## Reflexivity of virtual rack isomorphism

For every rack $R$ and every permutation $f$ of
$R$, the pair $(R, f)$ is isomorphic to itself in the sense of virtual rack isomorphism. The
permutation $f$ need not be a rack automorphism.

## Sources

- Lực Ta, *Enumeration of Virtual Quandles Up to Isomorphism*, Journal of Integer Sequences 28 (2025), Article 25.8.4, Section 2.2 (virtual rack isomorphisms).

Formalized by `MetaMathlibExt.virtualRackIso_refl`, a theorem declared in [WantedExt/Algebra/VirtualQuandleWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/VirtualQuandleWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/virtual-racks-and-quandles/index.html#virtual-rack-iso-refl).

## Affine maps are automorphisms of the dihedral quandle

For every natural number $n$,
every $a \in \mathbb{Z}/n\mathbb{Z}$ and every unit $u \in (\mathbb{Z}/n\mathbb{Z})^\times$, the
affine map $T_{a,u} \colon x \mapsto a + u x$ is a rack automorphism of the dihedral quandle
$R_n$, the set $\mathbb{Z}/n\mathbb{Z}$ with $x \triangleleft y = 2x - y$.

## Sources

- Lực Ta, *Enumeration of Virtual Quandles Up to Isomorphism*, Journal of Integer Sequences 28 (2025), Article 25.8.4, Section 2.2 (virtual structures on the dihedral quandle).

Formalized by `MetaMathlibExt.dihedralAffinePerm_mem_rackAut`, a theorem declared in [WantedExt/Algebra/VirtualQuandleWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/VirtualQuandleWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/virtual-racks-and-quandles/index.html#dihedral-affine-perm-mem-rack-aut).

## Multiplication action of the units of $\mathbb{Z}/n\mathbb{Z}$

For a natural number
$n$, the group homomorphism from the unit group $(\mathbb{Z}/n\mathbb{Z})^\times$ to the
automorphism group of the additive group $\mathbb{Z}/n\mathbb{Z}$ that sends a unit $u$ to
multiplication by $u$, the automorphism $x \mapsto u x$.

## Sources

- Lực Ta, *Enumeration of Virtual Quandles Up to Isomorphism*, Journal of Integer Sequences 28 (2025), Article 25.8.4, Section 4 (the holomorph `A ⋊ A^×`, `A = ℤ/nℤ`).

Formalized by `MetaMathlibExt.zmodUnitsMulAut`, a definition declared in [WantedExt/Algebra/VirtualQuandleWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/VirtualQuandleWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/virtual-racks-and-quandles/index.html#zmod-units-mul-aut).

## Holomorph of $\mathbb{Z}/n\mathbb{Z}$

For a natural number $n$, let
$A = \mathbb{Z}/n\mathbb{Z}$. The holomorph of $A$ is the semidirect product $A \rtimes A^\times$
in which the unit group $A^\times$ acts on $A$ by multiplication. Its elements are the pairs
$(a, u)$ with $a \in A$ and $u \in A^\times$, with product $(a, u)(b, v) = (a + u b, u v)$.

## Sources

- Lực Ta, *Enumeration of Virtual Quandles Up to Isomorphism*, Journal of Integer Sequences 28 (2025), Article 25.8.4, Section 4.

Formalized by `MetaMathlibExt.cyclicHolomorph`, an abbreviation declared in [WantedExt/Algebra/VirtualQuandleWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/VirtualQuandleWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/virtual-racks-and-quandles/index.html#cyclic-holomorph).

## Multiplication in the holomorph of $\mathbb{Z}/n\mathbb{Z}$

For a natural number $n$, let
$A = \mathbb{Z}/n\mathbb{Z}$ and write $(a, u)$ for the element of the holomorph
$A \rtimes A^\times$ with $a \in A$ and $u \in A^\times$. For all $a, b \in A$ and
$u, v \in A^\times$, $(a, u)(b, v) = (a + u b, u v)$.

## Sources

- Lực Ta, *Enumeration of Virtual Quandles Up to Isomorphism*, Journal of Integer Sequences 28 (2025), Article 25.8.4, proof of Proposition 22.

Formalized by `MetaMathlibExt.cyclicHolomorph_mk_mul_mk`, a theorem declared in [WantedExt/Algebra/VirtualQuandleWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/VirtualQuandleWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/virtual-racks-and-quandles/index.html#cyclic-holomorph-mk-mul-mk).

## Isomorphism of virtual structures is conjugacy

Let $R$ be a rack and let $f_1$ and $f_2$
be elements of its automorphism group $\operatorname{Aut} R$. Then the virtual racks $(R, f_1)$
and $(R, f_2)$ are isomorphic if and only if $f_1$ and $f_2$ are conjugate in
$\operatorname{Aut} R$.

## Sources

- Lực Ta, *Enumeration of Virtual Quandles Up to Isomorphism*, Journal of Integer Sequences 28 (2025), Article 25.8.4, Proposition 14 (`jis-2025-25.8.4-prop-14`).

Stated but not proved: `MetaMathlibExt.virtualRackIso_iff_isConj` is written with `theorem_wanted` in [WantedExt/Algebra/VirtualQuandleWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/VirtualQuandleWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/virtual-racks-and-quandles/index.html#virtual-rack-iso-iff-is-conj).

## Trivial center and automorphisms of the conjugation quandle

For a group $G$, let
$\operatorname{Conj}(G)$ be the conjugation quandle on $G$, with $x \triangleleft y = x y x^{-1}$.
Then $G$ has trivial center if and only if the permutations of $G$ that are group automorphisms
are exactly the rack automorphisms of $\operatorname{Conj}(G)$.

## Sources

- Lực Ta, *Enumeration of Virtual Quandles Up to Isomorphism*, Journal of Integer Sequences 28 (2025), Article 25.8.4, Lemma 17 (`jis-2025-25.8.4-lem-17`), quoting Bardakov, Nasybullov, and Singh, Corollary 2.

Stated but not proved: `MetaMathlibExt.center_eq_bot_iff_mulAut_eq_rackAut_conj` is written with `theorem_wanted` in [WantedExt/Algebra/VirtualQuandleWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/VirtualQuandleWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/virtual-racks-and-quandles/index.html#center-eq-bot-iff-mul-aut-eq-rack-aut-co).

## Isomorphism of affine virtual dihedral quandles

Let $n > 0$, let $R_n$ be the dihedral
quandle on $\mathbb{Z}/n\mathbb{Z}$ (with $x \triangleleft y = 2x - y$), and for
$a \in \mathbb{Z}/n\mathbb{Z}$ and $u \in (\mathbb{Z}/n\mathbb{Z})^\times$ let $T_{a,u}$ be the
permutation $x \mapsto a + u x$ of $R_n$. For all $a, b \in \mathbb{Z}/n\mathbb{Z}$ and
$u, v \in (\mathbb{Z}/n\mathbb{Z})^\times$, the virtual racks $(R_n, T_{a,u})$ and
$(R_n, T_{b,v})$ are isomorphic if and only if $u = v$ and $b = y a + (1 - u) x$ for some
$x \in \mathbb{Z}/n\mathbb{Z}$ and $y \in (\mathbb{Z}/n\mathbb{Z})^\times$.

## Sources

- Lực Ta, *Enumeration of Virtual Quandles Up to Isomorphism*, Journal of Integer Sequences 28 (2025), Article 25.8.4, Proposition 21 (`jis-2025-25.8.4-prop-21`).

Stated but not proved: `MetaMathlibExt.dihedral_virtualRackIso_iff` is written with `theorem_wanted` in [WantedExt/Algebra/VirtualQuandleWanted.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/VirtualQuandleWanted.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/virtual-racks-and-quandles/index.html#dihedral-virtual-rack-iso-iff).

## Conjugacy in the holomorph of $\mathbb{Z}/n\mathbb{Z}$

Let $n > 0$, let
$A = \mathbb{Z}/n\mathbb{Z}$, and write $(a, u)$ for the element of the holomorph
$A \rtimes A^\times$ with $a \in A$ and $u \in A^\times$. Two elements $(a, u)$ and $(b, v)$ are
conjugate if and only if $u = v$ and there is a unit $y \in A^\times$ with $b \equiv y a$ modulo
the ideal $(1 - u)A$ generated by $1 - u$.

## Sources

- Lực Ta, *Enumeration of Virtual Quandles Up to Isomorphism*, Journal of Integer Sequences 28 (2025), Article 25.8.4, Proposition 22 (`jis-2025-25.8.4-prop-22`).

Stated but not proved: `MetaMathlibExt.cyclicHolomorph_isConj_iff` is written with `theorem_wanted` in [WantedExt/Algebra/VirtualQuandleWanted.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/VirtualQuandleWanted.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/virtual-racks-and-quandles/index.html#cyclic-holomorph-is-conj-iff).

## Class number of the holomorph of $\mathbb{Z}/n\mathbb{Z}$

For every integer $n > 0$,
the number of conjugacy classes of the holomorph
$\mathbb{Z}/n\mathbb{Z} \rtimes (\mathbb{Z}/n\mathbb{Z})^\times$ of $\mathbb{Z}/n\mathbb{Z}$ equals
$\varphi(n) \sum_{d \mid n} 1/\varphi(d)$, where $\varphi$ is Euler's totient function.

## Sources

- Lực Ta, *Enumeration of Virtual Quandles Up to Isomorphism*, Journal of Integer Sequences 28 (2025), Article 25.8.4, Theorem 23 (`jis-2025-25.8.4-thm-23`).

Stated but not proved: `MetaMathlibExt.card_conjClasses_cyclicHolomorph` is written with `theorem_wanted` in [WantedExt/Algebra/VirtualQuandleWanted.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/VirtualQuandleWanted.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/virtual-racks-and-quandles/index.html#card-conj-classes-cyclic-holomorph).

## Virtual quandle structures on the dihedral quandle

For every $n > 0$, the number
$v(R_n)$ of isomorphism classes of virtual racks whose underlying rack is the dihedral quandle
$R_n$ (the set $\mathbb{Z}/n\mathbb{Z}$ with $x \triangleleft y = 2x - y$) equals
$\varphi(n) \sum_{d \mid n} 1/\varphi(d)$, where $\varphi$ is Euler's totient function.

## Sources

- Lực Ta, *Enumeration of Virtual Quandles Up to Isomorphism*, Journal of Integer Sequences 28 (2025), Article 25.8.4, Theorem 1 (`jis-2025-25.8.4-thm-1`).

Stated but not proved: `MetaMathlibExt.virtualRackClassCount_dihedral` is written with `theorem_wanted` in [WantedExt/Algebra/VirtualQuandleWanted.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/VirtualQuandleWanted.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/virtual-racks-and-quandles/index.html#virtual-rack-class-count-dihedral).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Virtual racks and quandles](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/virtual-racks-and-quandles/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Algebra/nonassociative-algebras/virtual-racks-and-quandles)
