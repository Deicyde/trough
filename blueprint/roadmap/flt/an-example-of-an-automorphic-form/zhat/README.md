# Zhat

Classically automorphic forms were defined as functions on symmetric spaces (like the upper half plane) which transformed well under the action of certain discrete groups (for example $\operatorname{SL}_2(\mathbb{Z})$). However such definitions became combinatorially problematic when generalised to number fields with nontrivial class group, because the classical theory needed a *number* $p$ to define the Hecke operator $T_p$, and in the case where $p$ was a non-principal prime ideal in a number field, there was no appropriate number. One fix is to take disjoint unions of symmetric spaces indexed by the ideal class group of the field in question, but it is easier to work adelically, which is morally what we shall do. However we are able to avoid introducing the adeles explicitly; we can work instead with the conceptually simpler object $\widehat{\mathbb{Z}}$, the profinite completion of $\mathbb{Z}$. So what is $\widehat{\mathbb{Z}}$? We offer a low-level definition of this object.

Given an integer $z$, we can reduce it mod $N$ for every positive natural number and get elements $z_N=\overline{z}\in\mathbb{Z}/N\mathbb{Z}$. These elements are not completely arbitrary though – they must satisfy some compatibility conditions. For example there can be no positive integer $z$ such that $z_{10}=6$ and $z_2=1$, because $z_{10}=6$ tells us that $z$ ends in a 6 when written in base 10, and in particular it's even, so $z_2$ must be 0. The general rule: if $D\mid N$ then $z_D$ must be equal to image of $z_N$ under the natural ring homomorphism from $\mathbb{Z}/N\mathbb{Z}$ to $\mathbb{Z}/D\mathbb{Z}$. We say that a collection of elements $z_N\in\mathbb{Z}/N\mathbb{Z}$ is *compatible* if it satisfies this rule.

- [ZHat](zhat.md)
- [ZHat.commRing](zhat-commring.md)
- [ZHat.nontrivial](zhat-nontrivial.md)
- [ZHat.charZero](zhat-charzero.md)
- [ZHat.e](zhat-e.md)
- [ZHat.e\_def](zhat-e-def.md)
- [ZHat.e\_not\_in\_Int](zhat-e-not-in-int.md)
- [ZHat.torsionfree](zhat-torsionfree.md)
- [ZHat.multiples](zhat-multiples.md)
