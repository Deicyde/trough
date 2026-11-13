---
declaration: section
origin: cited
lean: FractionalIdeal.absNorm_units_ne_zero, FractionalIdeal.absNorm_units_pos, NumberField.ArakelovDivisor, NumberField.ArakelovDivisor.archimedeanFactor, NumberField.ArakelovDivisor.archimedeanFactor_coe, NumberField.ArakelovDivisor.idealNorm, NumberField.ArakelovDivisor.idealNorm_coe, NumberField.ArakelovDivisor.archHom
statement: formalized
proof: formalized
---

# Arakelov divisors

25 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/arakelov-divisors/index.html).

## Invertible fractional ideals have nonzero absolute norm

Let $R$ be a Dedekind domain
that is a free $\mathbb{Z}$-module of finite rank, and let $F$ be its field of fractions. For
every invertible fractional ideal $I$ of $R$ in $F$, the absolute norm of $I$, a rational
number, is nonzero.

Formalized by `FractionalIdeal.absNorm_units_ne_zero`, a theorem declared in [MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/arakelov-divisors/index.html#abs-norm-units-ne-zero).

## Invertible fractional ideals have positive absolute norm

Let $R$ be a Dedekind domain
that is a free $\mathbb{Z}$-module of finite rank, and let $F$ be its field of fractions. For
every invertible fractional ideal $I$ of $R$ in $F$, the absolute norm of $I$, a rational
number, is positive.

Formalized by `FractionalIdeal.absNorm_units_pos`, a theorem declared in [MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/arakelov-divisors/index.html#abs-norm-units-pos).

## Arakelov divisor

Let $K$ be a number field with ring of integers $\mathcal{O}_K$. An
Arakelov divisor on $K$ is a pair $(I, r)$, where $I$ is an invertible fractional ideal of
$\mathcal{O}_K$ in $K$ and $r$ assigns a positive real number $r_w$ to each infinite place $w$
of $K$.

Formalized by `NumberField.ArakelovDivisor`, an abbreviation declared in [MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/arakelov-divisors/index.html#arakelov-divisor).

## Archimedean factor

Let $D = (I, r)$ be an Arakelov divisor on a number field $K$. Its
archimedean factor is the positive real number $\prod_w r_w^{m_w}$, where the product runs over
all infinite places $w$ of $K$ and $m_w$ is $1$ if $w$ is real and $2$ if $w$ is complex.

Formalized by `NumberField.ArakelovDivisor.archimedeanFactor`, a definition declared in [MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/arakelov-divisors/index.html#archimedean-factor).

## Archimedean factor as a real number

Let $D = (I, r)$ be an Arakelov divisor on a number
field $K$, and for each infinite place $w$ of $K$ let $m_w$ be $1$ if $w$ is real and $2$ if $w$
is complex. Viewed as a real number, the archimedean factor of $D$ equals the real product
$\prod_w r_w^{m_w}$ over all infinite places $w$ of $K$.

Formalized by `NumberField.ArakelovDivisor.archimedeanFactor_coe`, a theorem declared in [MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/arakelov-divisors/index.html#archimedean-factor-coe).

## Ideal norm of an Arakelov divisor

For an Arakelov divisor $D$ of a number field $K$ with
invertible fractional ideal $I$, the ideal norm of $D$ is the absolute norm $N(I)$ of $I$,
regarded as a positive real number; it is positive because $I$ is invertible.

Formalized by `NumberField.ArakelovDivisor.idealNorm`, a definition declared in [MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/arakelov-divisors/index.html#ideal-norm).

## Real value of the ideal norm

For every Arakelov divisor $D$ of a number field $K$ with
fractional ideal $I$, the ideal norm of $D$, viewed as a real number, equals the absolute norm
$N(I) \in \mathbb{Q}$ of $I$, viewed as a real number.

Formalized by `NumberField.ArakelovDivisor.idealNorm_coe`, a theorem declared in [MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/arakelov-divisors/index.html#ideal-norm-coe).

## Archimedean factor homomorphism

For a number field $K$, the map sending an Arakelov
divisor on $K$ to its archimedean factor is a monoid homomorphism from the Arakelov divisors on
$K$, multiplied componentwise, to the positive real numbers under multiplication.

Formalized by `NumberField.ArakelovDivisor.archHom`, a definition declared in [MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/arakelov-divisors/index.html#arch-hom).

## Ideal norm homomorphism

For a number field $K$, the map sending an Arakelov divisor
$(I, r)$ on $K$ to the absolute norm of $I$, viewed as a positive real number, is a monoid
homomorphism from the Arakelov divisors on $K$, multiplied componentwise, to the positive real
numbers under multiplication.

Formalized by `NumberField.ArakelovDivisor.idealHom`, a definition declared in [MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/arakelov-divisors/index.html#ideal-hom).

## Size of an Arakelov divisor

For a number field $K$, the size homomorphism sends an
Arakelov divisor $D = (I, (r_w)_w)$, with $I$ an invertible fractional ideal of the ring of
integers of $K$ and $r_w > 0$ for each infinite place $w$, to the positive real number
$\prod_w r_w^{m_w} / N(I)$, where $w$ runs over the infinite places of $K$, $m_w$ is $1$ for a
real place and $2$ for a complex place, and $N(I)$ is the absolute norm of $I$. It is a group
homomorphism from Arakelov divisors to the multiplicative group of positive reals.

Formalized by `NumberField.ArakelovDivisor.sizeHom`, a definition declared in [MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/arakelov-divisors/index.html#size-hom).

## Size as a quotient of homomorphisms

For every Arakelov divisor $D$ of a number field
$K$, the size of $D$ equals the archimedean-factor homomorphism evaluated at $D$ divided by the
ideal-norm homomorphism evaluated at $D$, the quotient taken in the group of positive reals.

Formalized by `NumberField.ArakelovDivisor.sizeHom_apply`, a theorem declared in [MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/arakelov-divisors/index.html#size-hom-apply).

## Explicit formula for the size of an Arakelov divisor

Let $D = (I, (r_w)_w)$ be an
Arakelov divisor of a number field $K$, where $I$ is an invertible fractional ideal of the ring
of integers of $K$ and $r_w > 0$ for each infinite place $w$ of $K$. For each $w$ let $m_w$ be
$1$ if $w$ is real and $2$ if $w$ is complex, and let $N(I)$ be the absolute norm of $I$. Then
the size of $D$, as a real number, is

$$\frac{\prod_w r_w^{m_w}}{N(I)},$$

where the product runs over all infinite places $w$ of $K$.

Formalized by `NumberField.ArakelovDivisor.sizeHom_coe`, a theorem declared in [MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/arakelov-divisors/index.html#size-hom-coe).

## Section set of an Arakelov divisor

Let $D$ be an Arakelov divisor of a number field $K$,
with invertible fractional ideal $I$ and positive real number $r_w$ at each infinite place $w$
of $K$. The section set of $D$ is the set of $x \in I$ such that $w(x) \le r_w$ for every
infinite place $w$ of $K$.

At a complex place the bound is on $w(x)$ itself, not on $w(x)^2$; the squaring at complex
places enters only in the size of $D$.

Formalized by `NumberField.ArakelovDivisor.sectionSet`, a definition declared in [MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/arakelov-divisors/index.html#section-set).

## Membership in the section set

Let $D$ be an Arakelov divisor of a number field $K$, with
invertible fractional ideal $I$ and positive real number $r_w$ at each infinite place $w$ of $K$.
An element $x \in K$ lies in the section set of $D$ if and only if $x \in I$ and
$w(x) \le r_w$ for every infinite place $w$ of $K$.

Formalized by `NumberField.ArakelovDivisor.mem_sectionSet`, a theorem declared in [MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/arakelov-divisors/index.html#mem-section-set).

## Finiteness of section sets

For every Arakelov divisor $D$ of a number field $K$, the
section set of $D$ is finite.

Multiplying by a nonzero $d \in \mathcal{O}_K$ that clears the denominators of the fractional
ideal of $D$ sends the section set into $\mathcal{O}_K$, and the bounds at the infinite places
give a uniform bound $B$ on $|\sigma(dx)|$ for all $x$ in the section set and all complex
embeddings $\sigma$ of $K$; only finitely many algebraic integers of $K$ have all conjugates of
absolute value at most $B$.

Formalized by `NumberField.ArakelovDivisor.sectionSet_finite`, a theorem declared in [MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/arakelov-divisors/index.html#section-set-finite).

## Archimedean part of a principal divisor

For a nonzero element $x$ of a number field $K$,
this is the family that assigns to each infinite place $w$ of $K$ the positive real
number $w(x)$.

Formalized by `NumberField.principalArch`, a definition declared in [MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/arakelov-divisors/index.html#principal-arch).

## Principal Arakelov divisor

For a nonzero element $x$ of a number field $K$, the principal
Arakelov divisor of $x$ consists of the principal fractional ideal $x\mathcal{O}_K$ together with
the positive real number $w(x)$ at each infinite place $w$ of $K$.

Formalized by `NumberField.principalDivisor`, a definition declared in [MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/arakelov-divisors/index.html#principal-divisor).

## Infinite component of a principal divisor

Let $K$ be a number field, $x \in K$ nonzero
and $w$ an infinite place of $K$. The positive real number that the principal Arakelov divisor
of $x$ assigns to $w$ is $w(x)$, the absolute value of $x$ at $w$.

Formalized by `NumberField.coe_principalDivisor_snd`, a theorem declared in [MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/arakelov-divisors/index.html#coe-principal-divisor-snd).

## Finite component of a principal divisor

Let $K$ be a number field with ring of integers
$\mathcal{O}_K$. For every nonzero $x \in K$, the fractional ideal component of the principal
Arakelov divisor of $x$ is the principal fractional ideal $x\mathcal{O}_K$.

Formalized by `NumberField.coe_principalDivisor_fst`, a theorem declared in [MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/arakelov-divisors/index.html#coe-principal-divisor-fst).

## Principal divisor homomorphism

For a number field $K$, the map sending a nonzero element
$x \in K$ to its principal Arakelov divisor is a group homomorphism from the multiplicative
group $K^\times$ to the group of Arakelov divisors of $K$.

Formalized by `NumberField.principalHom`, a definition declared in [MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/arakelov-divisors/index.html#principal-hom).

## Subgroup of principal Arakelov divisors

For a number field $K$, the principal subgroup is
the image of the principal divisor homomorphism, that is, the subgroup of the group of Arakelov
divisors of $K$ consisting of the principal Arakelov divisors of the nonzero elements of $K$.

Formalized by `NumberField.principalSubgroup`, a definition declared in [MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/arakelov-divisors/index.html#principal-subgroup).

## Degree-zero Arakelov divisors

For a number field $K$, the degree-zero subgroup of the
group of Arakelov divisors on $K$ is the kernel of the size homomorphism, that is, the subgroup
of Arakelov divisors of size $1$.

Formalized by `NumberField.degreeZero`, a definition declared in [MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/arakelov-divisors/index.html#degree-zero).

## Principal Arakelov divisors have size one

Let $K$ be a number field with ring of
integers $\mathcal{O}_K$. For every nonzero $x \in K$, the principal Arakelov divisor of $x$,
formed by the principal fractional ideal $x\mathcal{O}_K$ and the values $w(x)$ at the infinite
places $w$ of $K$, has size $1$.

This is the product formula: with $m_w$ equal to $1$ at real and $2$ at complex places, the
archimedean factor $\prod_w w(x)^{m_w}$ equals $|N_{K/\mathbb{Q}}(x)|$, where $N_{K/\mathbb{Q}}$
is the field norm from $K$ to $\mathbb{Q}$, and so does the absolute norm of $x\mathcal{O}_K$.

Formalized by `NumberField.size_principal`, a theorem declared in [MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/arakelov-divisors/index.html#size-principal).

## Principal Arakelov divisors have degree zero

For a number field $K$, the subgroup of
principal Arakelov divisors of $K$ is contained in the degree-zero subgroup.

Formalized by `NumberField.principalSubgroup_le_degreeZero`, a theorem declared in [MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean, line 307](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/ArakelovDivisor.lean#L307). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/arakelov-divisors/index.html#principal-subgroup-le-degree-zero).

## Large Arakelov divisors have a nonzero section

Let $K$ be a number field with $s$
complex places and discriminant $d_K$, and let $D$ be an Arakelov divisor on $K$. If the size
of $D$ is strictly greater than $(2/\pi)^s \sqrt{|d_K|}$, then the section set of $D$ contains
a nonzero element of $K$.

## Sources

- Proposition 15.9 of ATLAS `NumberTheoryI`.

Formalized by `NumberField.ArakelovDivisor.exists_ne_zero_mem_sectionSet_of_size_gt`, a theorem declared in [MathlibExt/NumberTheory/NumberField/ArakelovDivisor/NonzeroSection.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/ArakelovDivisor/NonzeroSection.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/arakelov-divisors/index.html#exists-ne-zero-mem-section-set-of-size-g).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Arakelov divisors](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/arakelov-divisors/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/arakelov-divisors)
