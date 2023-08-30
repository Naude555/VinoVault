from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Wine


class WineListView(LoginRequiredMixin, ListView):
    """
    Display a list of wines in the inventory.
    """

    model = Wine
    template_name = "vinventory/wine_list.html"
    context_object_name = "wines"

    def get_queryset(self):
        """
        Return the wines filtered by the logged-in user.
        """
        return Wine.objects.filter(user=self.request.user)

    def get_success_url(self):
        """
        Return the URL to redirect to after successful operations.
        """
        return reverse_lazy("vinventory:wine_list")

    def drink_wine(self, pk):
        """
        Decrease the quantity of a wine and save the changes.
        """
        wine = Wine.objects.get(pk=pk)
        if wine.quantity > 0:
            wine.quantity -= 1
            wine.save()
        return HttpResponseRedirect(
            self.request.META.get("HTTP_REFERER", "/")
        )  # Redirect back to the same page

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests, including the 'drink' action.
        """
        if "drink" in request.POST:
            wine_pk = request.POST.get("wine_pk")
            self.drink_wine(wine_pk)
        return self.get(request, *args, **kwargs)


class WineUpdateView(LoginRequiredMixin, UpdateView):
    """
    View to update an existing wine entry in the inventory.

    This view inherits from Django's UpdateView and requires user authentication.

    :Attributes:
        - model: The model class representing Wine data.
        - template_name: The name of the template for the wine update form.
        - fields: The fields to be displayed in the update form.

    :Methods:
        - get_queryset(): Return a queryset of wines filtered by the logged-in user.
        - get_success_url(): Return the URL to redirect to after successful update.
    """

    model = Wine
    template_name = "vinventory/wine_form.html"
    fields = [
        "name",
        "variety",
        "region",
        "year",
        "quantity",
        "received_from",
        "date_received",
        "date_to_drink_start",
        "date_to_drink_end",
    ]

    def get_queryset(self):
        """
        Return a queryset of wines filtered by the logged-in user.

        :returns: A queryset of Wine objects.
        :rtype: QuerySet
        """
        return Wine.objects.filter(user=self.request.user)

    def get_success_url(self):
        """
        Return the URL for redirection after successful update.

        :returns: The URL for the wine list view.
        :rtype: str
        """
        return reverse_lazy("vinventory:wine_list")


class WineUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update an existing wine entry in the inventory.
    """

    model = Wine
    template_name = "vinventory/wine_form.html"
    fields = [
        "name",
        "variety",
        "region",
        "year",
        "quantity",
        "received_from",
        "date_received",
        "date_to_drink_start",
        "date_to_drink_end",
    ]

    def get_queryset(self):
        """
        Return the wines filtered by the logged-in user.
        """
        return Wine.objects.filter(user=self.request.user)

    def get_success_url(self):
        """
        Return the URL to redirect to after successful update.
        """
        return reverse_lazy("vinventory:wine_list")


class WineDeleteView(LoginRequiredMixin, DeleteView):
    """
    View to delete a wine entry from the inventory.

    This view inherits from Django's DeleteView and requires user authentication.

    :Attributes:
        - model: The model class representing Wine data.
        - template_name: The name of the template for the deletion confirmation page.
        - success_url: The URL to redirect to after successful deletion.

    :Methods:
        - get_queryset(): Return a queryset of wines filtered by the logged-in user.
        - get_success_url(): Return the URL to redirect to after successful deletion.
    """

    model = Wine
    template_name = "vinventory/wine_confirm_delete.html"
    success_url = reverse_lazy("vinventory:wine_list")

    def get_queryset(self):
        """
        Return a queryset of wines filtered by the logged-in user.

        :returns: A queryset of Wine objects.
        :rtype: QuerySet
        """
        return Wine.objects.filter(user=self.request.user)

    def get_success_url(self):
        """
        Return the URL for redirection after successful deletion.

        :returns: The URL for the wine list view.
        :rtype: str
        """
        return reverse_lazy("vinventory:wine_list")
