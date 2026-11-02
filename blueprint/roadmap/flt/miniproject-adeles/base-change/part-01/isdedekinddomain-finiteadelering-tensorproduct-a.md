---
declaration: corollary
origin: cited
---

# IsDedekindDomain.FiniteAdeleRing.tensorProduct\_algEquiv

The natural map $B\otimes_AK\to L$ is a $B$-algebra isomorphism.

## Depends on

- [IsDedekindDomain.dvd\_norm](isdedekinddomain-dvd-norm.md)

## Proof

We write down an inverse. Regard $B\otimes_AK$ as a $B$-algebra via the action on the left. Note that at this point it's not even clear that $B\otimes_AK$ is a field. We have the structure map $B\to B\otimes_AK$ sending $b$ to $b\otimes1$, which is $B$-linear. I claim that every nonzero element of $B$ gets sent to an invertible element of $B\otimes_AK$. Indeed, if $b\not=0$ and (using the previous lemma) we choose $0\not=a\in A$ such that $bb'=a$, then $(b\otimes1)(b'\otimes\frac1a)=1$. Thus by the universal property of localisation, the $B$-linear map $B\to B\otimes_AK$ extends to a ring homomorphism from the field of fractions of $B$ to $B\otimes_AK$, which we claim is our desired inverse. Checking that both composites are the identity should be straightforward. Starting with $B\otimes_AK$ we only have to check on elements of the form $b\otimes k$; starting with $L$ we only have to check on elements of $B$. Hopefully both are straightforward.

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/AdeleMiniproject.tex, line 461](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/AdeleMiniproject.tex#L461)
