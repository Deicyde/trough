---
declaration: lemma
origin: cited
lean: QHat.unitsrat_join_unitszHat
statement: formalized
proof: formalized
---

# QHat.unitsrat_join_unitszHat

The product of $\mathbb{Q}^\times$ and $\widehat{\mathbb{Z}}^\times$ in $\widehat{\mathbb{Q}}^\times$ is all of $\widehat{\mathbb{Q}}^\times$. More precisely, every element of $\widehat{\mathbb{Q}}^\times$ can be written as $qz$ with $q\in\mathbb{Q}^\times$ and $z\in\widehat{\mathbb{Z}}^\times$.

## Depends on

- [QHat](../widehat-q-and-tensor-products/qhat.md)
- [ZHat.commRing](../widehat-z/zhat-commring.md)

## Proof depends on

- [ZHat.multiples](../widehat-z/zhat-multiples.md)
- [QHat.canonicalForm](../a-crash-course-in-tensor-products/qhat-canonicalform.md)

## Proof

We already know that a general element of $\widehat{\mathbb{Q}}^\times$ can be written as $x/N$ with $N$ positive, so this reduces us to proving that a general element $x\in\widehat{\mathbb{Z}}$ which is invertible in $\widehat{\mathbb{Q}}^\times$ can be written as $qz$ with $q\in\mathbb{Q}^\times$ and $z\in\widehat{\mathbb{Z}}^\times$.

We know $1/x$ can be written in lowest terms as $y/M$, and multiplying up we deduce that $xy=M$, and hence $x$ divides a positive integer. If $i:\mathbb{Z}\to\widehat{\mathbb{Z}}$ denotes the inclusion, then we've just seen that the preimage of the principal ideal $(x)$, namely, $J:=i^{-1}(x\widehat{\mathbb{Z}})$ is nonzero, as it contains $M$. Let $g\in J$ be the smallest positive integer; it's well-known that $J=(g)$.

I claim that it suffices to show that $x\widehat{\mathbb{Z}}=g\widehat{\mathbb{Z}}$. Because knowing $g=yx$ and $x=gz$ for some $y,z\in\widehat{\mathbb{Z}}$ tells us that $g(1-yz)=0$, and we know that multiplication by $g$ is injective, hence $yz=1$, so $z$ is a unit and we have written $x=gz$ with $g\in\mathbb{Q}^\times$ and $z\in\widehat{\mathbb{Z}}^\times$.

It remains to prove the claim. By definition $g\in J\subseteq x\widehat{\mathbb{Z}}$ so this is one inclusion. For the other, it suffices to prove that $x_g=0$. However if $0\lt x_g\lt g$ lifts $x_g$ to the naturals then I claim that $x_g\in J$, for $x_g-x$ is a multiple of $g$ and hence of $x$, and this contradicts minimality of $g$.

## Lean

Formalized as [`QHat.unitsrat_join_unitszHat`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/QHat.unitsrat_join_unitszHat).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/ch05automorphicformexample.tex, line 503](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/ch05automorphicformexample.tex#L503)
