---
declaration: section
origin: cited
---

# Primitive roots modulo prime powers

12 results, 12 whose declaration the Lean read here does not declare, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/primitive-roots-modulo-prime-powers/index.html).

## Multiplicative order modulo $n$

For natural numbers $n$ and $a$,
$\operatorname{ord}_n(a)$ is the multiplicative order of the residue class of $a$ in the
unit group $(\mathbb{Z}/n\mathbb{Z})^\times$ when $a$ is coprime to $n$, and $0$
otherwise.

Formalized by `MathlibExt.NumberTheory.GaussPrimitiveRootsWanted.mulOrdMod`, which the repository's Lean, as read here, does not declare. [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/primitive-roots-modulo-prime-powers/index.html#mul-ord-mod).

## Reduction of units modulo $p^2$ to units modulo $p$

For a natural number $p$, this is
the group homomorphism $(\mathbb{Z}/p^2\mathbb{Z})^\times \to (\mathbb{Z}/p\mathbb{Z})^\times$
induced on units by the reduction ring homomorphism
$\mathbb{Z}/p^2\mathbb{Z} \to \mathbb{Z}/p\mathbb{Z}$, which sends the class of $x$ modulo $p^2$ to
the class of $x$ modulo $p$.

Formalized by `MathlibExt.NumberTheory.GaussPrimitiveRootsWanted.unitReduceSq`, which the repository's Lean, as read here, does not declare. [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/primitive-roots-modulo-prime-powers/index.html#unit-reduce-sq).

## Fibers of reduction modulo $p$ on units modulo $p^2$

For a natural number $p$ and a unit
$a$ of $\mathbb{Z}/p^2\mathbb{Z}$, the fiber $P_a$ is the set of units $x$ of
$\mathbb{Z}/p^2\mathbb{Z}$ with $x \equiv a \pmod p$, that is, the units whose image under the
reduction map $(\mathbb{Z}/p^2\mathbb{Z})^\times \to (\mathbb{Z}/p\mathbb{Z})^\times$ equals the
image of $a$.

Formalized by `MathlibExt.NumberTheory.GaussPrimitiveRootsWanted.liftFiber`, which the repository's Lean, as read here, does not declare. [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/primitive-roots-modulo-prime-powers/index.html#lift-fiber).

## The order of $a + kp$ modulo $p^2$

Let $p$ be an odd prime and let $a$ and $k$ be
natural numbers with $a$ coprime to $p$. Writing $\operatorname{ord}_n(b)$ for the
multiplicative order of $b$ modulo $n$, the order $\operatorname{ord}_{p^2}(a + kp)$ is
either $\operatorname{ord}_p(a)$ or $p \cdot \operatorname{ord}_p(a)$.

## Sources

- V. P. Ramesh and S. Sivakumar, "A Note on Gauss's Theorem on the Primitive Roots Modulo `p^ℓ`", Lemma 1.

Formalized by `MathlibExt.NumberTheory.GaussPrimitiveRootsWanted.order_add_mul_prime_eq_or_mul`, which the repository's Lean, as read here, does not declare. [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/primitive-roots-modulo-prime-powers/index.html#order-add-mul-prime-eq-or-mul).

## Unique order-preserving lift modulo $p^2$

Let $p$ be an odd prime and let $a$ be
a natural number coprime to $p$. Writing $\operatorname{ord}_n(b)$ for the multiplicative
order of $b$ modulo $n$, there is exactly one $m \in \{0, 1, \dots, p - 1\}$ such that
$\operatorname{ord}_{p^2}(a + mp) = \operatorname{ord}_p(a)$.

## Sources

- V. P. Ramesh and S. Sivakumar, "A Note on Gauss's Theorem on the Primitive Roots Modulo `p^ℓ`", Theorem 2.

Formalized by `MathlibExt.NumberTheory.GaussPrimitiveRootsWanted.existsUnique_order_add_mul_prime_eq`, which the repository's Lean, as read here, does not declare. [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/primitive-roots-modulo-prime-powers/index.html#exists-unique-order-add-mul-prime-eq).

## Unique order-preserving element of a fiber modulo $p^2$

Let $p$ be an odd prime,
let $x_0$ be a unit modulo $p^2$, and let $P_{x_0}$ be the set of units $x$ modulo $p^2$
with $x \equiv x_0 \pmod p$. There is exactly one $x \in P_{x_0}$ whose multiplicative
order modulo $p^2$ equals the multiplicative order of its reduction modulo $p$.

## Sources

- V. P. Ramesh and S. Sivakumar, "A Note on Gauss's Theorem on the Primitive Roots Modulo `p^ℓ`", Theorem 2.

Formalized by `MathlibExt.NumberTheory.GaussPrimitiveRootsWanted.existsUnique_mem_liftFiber_order_eq`, which the repository's Lean, as read here, does not declare. [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/primitive-roots-modulo-prime-powers/index.html#exists-unique-mem-lift-fiber-order-eq).

## Gauss's theorem on primitive roots modulo prime powers

Let $p$ be an odd prime
and let $g$ be a natural number that is a primitive root modulo $p$, where a primitive
root modulo $n$ is a residue class modulo $n$ of multiplicative order $\varphi(n)$. Then
there is a natural number $k$ such that $g + kp$ is a primitive root modulo $p^\ell$ for
every $\ell \ge 2$.

## Sources

- V. P. Ramesh and S. Sivakumar, "A Note on Gauss's Theorem on the Primitive Roots Modulo `p^ℓ`", Theorem 1.

Formalized by `MathlibExt.NumberTheory.GaussPrimitiveRootsWanted.exists_primitiveRoot_add_mul_prime_pow`, which the repository's Lean, as read here, does not declare. [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/primitive-roots-modulo-prime-powers/index.html#exists-primitive-root-add-mul-prime-pow).

## Exactly one lift of a primitive root fails modulo $p^2$

Let $p$ be an odd prime
and let $g$ be a natural number that is a primitive root modulo $p$, where a primitive
root modulo $n$ is a residue class modulo $n$ of multiplicative order $\varphi(n)$. Then
there is exactly one $m \in \{0, 1, \dots, p - 1\}$ such that $g + mp$ is not a primitive
root modulo $p^2$, and $g + kp$ is a primitive root modulo $p^2$ for every other
$k \in \{0, 1, \dots, p - 1\}$.

## Sources

- V. P. Ramesh and S. Sivakumar, "A Note on Gauss's Theorem on the Primitive Roots Modulo `p^ℓ`", Corollary 1.

Formalized by `MathlibExt.NumberTheory.GaussPrimitiveRootsWanted.existsUnique_not_primitiveRoot_add_mul_prime`, which the repository's Lean, as read here, does not declare. [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/primitive-roots-modulo-prime-powers/index.html#exists-unique-not-primitive-root-add-mul).

## The lift of order $p - 1$ of a primitive root

Let $p$ be an odd prime and let
$g$ be a natural number that is a primitive root modulo $p$, that is, a residue class
modulo $p$ of multiplicative order $\varphi(p) = p - 1$. Let $P_g$ be the set of units
$x$ modulo $p^2$ with $x \equiv g \pmod p$. Then exactly one $x \in P_g$ has
multiplicative order $p - 1$ modulo $p^2$.

## Sources

- V. P. Ramesh and S. Sivakumar, "A Note on Gauss's Theorem on the Primitive Roots Modulo `p^ℓ`", Corollary 1.

Formalized by `MathlibExt.NumberTheory.GaussPrimitiveRootsWanted.existsUnique_mem_liftFiber_order_eq_sub_one`, which the repository's Lean, as read here, does not declare. [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/primitive-roots-modulo-prime-powers/index.html#exists-unique-mem-lift-fiber-order-eq-su).

## Primitive roots modulo $p^\ell$ of the form $g^p + kp$

Let $p$ be an odd prime and let
$g$ be a natural number that is a primitive root modulo $p$. If $k$ is a natural number not
divisible by $p$, then $g^p + kp$ is a primitive root modulo $p^\ell$ for every natural number
$\ell > 1$.

Here a natural number $a$ is a primitive root modulo $n$ when its residue class in
$\mathbb{Z}/n\mathbb{Z}$ is a primitive $\varphi(n)$-th root of unity, where $\varphi$ is Euler's
totient function.

## Sources

- V. P. Ramesh and S. Sivakumar, "A Note on Gauss's Theorem on the Primitive Roots Modulo `p^ℓ`", Theorem 3.

Formalized by `MathlibExt.NumberTheory.GaussPrimitiveRootsWanted.primitiveRoot_pow_add_mul_prime_pow`, which the repository's Lean, as read here, does not declare. [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/primitive-roots-modulo-prime-powers/index.html#primitive-root-pow-add-mul-prime-pow).

## Endomorphisms of the units modulo $p^2$ respect the fibers

Let $p$ be an odd
prime, let $f$ be a group endomorphism of $(\mathbb{Z}/p^2\mathbb{Z})^\times$, and let
$a$ be a unit modulo $p^2$. Writing $P_b$ for the set of units $x$ modulo $p^2$ with
$x \equiv b \pmod p$, the image of $P_a$ under $f$ is contained in $P_{f(a)}$.

## Sources

- V. P. Ramesh and S. Sivakumar, "A Note on Gauss's Theorem on the Primitive Roots Modulo `p^ℓ`", Lemma 3.

Formalized by `MathlibExt.NumberTheory.GaussPrimitiveRootsWanted.monoidHom_image_liftFiber_subset`, which the repository's Lean, as read here, does not declare. [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/primitive-roots-modulo-prime-powers/index.html#monoid-hom-image-lift-fiber-subset).

## Power maps on the fibers modulo $p^2$

Let $p$ be an odd prime, let $a$ be a unit
modulo $p^2$, and let $n$ be a natural number coprime to $p$ and to the multiplicative
order of $a$. Writing $P_b$ for the set of units $x$ modulo $p^2$ with
$x \equiv b \pmod p$, the map $x \mapsto x^n$ is injective on $P_a$, maps $P_a$ onto
$P_{a^n}$, and preserves the multiplicative order of every element of $P_a$.

## Sources

- V. P. Ramesh and S. Sivakumar, "A Note on Gauss's Theorem on the Primitive Roots Modulo `p^ℓ`", Lemma 4.

Formalized by `MathlibExt.NumberTheory.GaussPrimitiveRootsWanted.pow_injectiveOn_liftFiber_and_order_eq`, which the repository's Lean, as read here, does not declare. [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/primitive-roots-modulo-prime-powers/index.html#pow-injective-on-lift-fiber-and-order-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Primitive roots modulo prime powers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/primitive-roots-modulo-prime-powers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/primitive-roots-modulo-prime-powers)
