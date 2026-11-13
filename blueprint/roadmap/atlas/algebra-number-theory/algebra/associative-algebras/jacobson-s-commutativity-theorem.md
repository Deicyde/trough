---
declaration: section
origin: cited
lean: MathlibExt.Algebra.Ring.JacobsonCommutativity.IsPrimeIdeal, MathlibExt.Algebra.Ring.JacobsonCommutativity.IsMSystem, MathlibExt.Algebra.Ring.JacobsonCommutativity.jacobson_commutativity
statement: formalized
proof: formalized
---

# Jacobson's commutativity theorem

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/associative-algebras/jacobson-s-commutativity-theorem/index.html).

## Prime two-sided ideal

A two-sided ideal $P$ of a ring $R$ is prime if $P \ne R$ and,
for all $a, b \in R$, if $a r b \in P$ for every $r \in R$, then $a \in P$ or $b \in P$.

This is the noncommutative notion of primality; being completely prime ($P \ne R$, and
$ab \in P$ forces $a \in P$ or $b \in P$) is stronger.

Formalized by `MathlibExt.Algebra.Ring.JacobsonCommutativity.IsPrimeIdeal`, a definition declared in [MathlibExt/Algebra/Ring/JacobsonCommutativity.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Ring/JacobsonCommutativity.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/associative-algebras/jacobson-s-commutativity-theorem/index.html#is-prime-ideal).

## m-system

A subset $M$ of a ring $R$ is an $m$-system if it is nonempty, does not
contain $0$, and for all $a, b \in M$ there is some $r \in R$ with $a r b \in M$.

Formalized by `MathlibExt.Algebra.Ring.JacobsonCommutativity.IsMSystem`, a definition declared in [MathlibExt/Algebra/Ring/JacobsonCommutativity.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Ring/JacobsonCommutativity.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/associative-algebras/jacobson-s-commutativity-theorem/index.html#is-msystem).

## Jacobson's commutativity theorem

Let $R$ be a ring. If for every $x \in R$ there is a
natural number $n > 1$ with $x^n = x$, then $R$ is commutative, that is, $xy = yx$ for all
$x, y \in R$.

Formalized by `MathlibExt.Algebra.Ring.JacobsonCommutativity.jacobson_commutativity`, a theorem declared in [MathlibExt/Algebra/Ring/JacobsonCommutativity.lean, line 1555](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Ring/JacobsonCommutativity.lean#L1555). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/associative-algebras/jacobson-s-commutativity-theorem/index.html#jacobson-commutativity).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Jacobson's commutativity theorem](https://deicyde.github.io/atlas-lean/roadmap/Algebra/associative-algebras/jacobson-s-commutativity-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Algebra/associative-algebras/jacobson-s-commutativity-theorem)
