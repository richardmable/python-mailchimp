# coding=utf-8
"""
The List Member Notes API endpoint

Documentation: http://developer.mailchimp.com/documentation/mailchimp/reference/lists/members/notes/
Schema: https://api.mailchimp.com/schema/3.0/Lists/Members/Notes/Instance.json
"""
from __future__ import unicode_literals

from mailchimp3.baseapi import BaseApi


class ListMemberNote(BaseApi):
    """
    Retrieve recent notes for a specific list member.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(ListMemberNote, self).__init__(*args, **kwargs)
        self.endpoint = 'lists'
        self.list_id = None
        self.subscriber_hash = None
        self.note_id = None


    def create(self, list_id, subscriber_hash, data):
        """
        Add a new note for a specific subscriber.

        :param list_id: The unique id for the list.
        :type list_id: :py:class:`str`
        :param subscriber_hash: The MD5 hash of the lowercase version of the
          list member’s email address.
        :type subscriber_hash: :py:class:`str`
        :param data: The request body parameters
        :type data: :py:class:`dict`
        """
        self.list_id = list_id
        self.subscriber_hash = subscriber_hash
        response = self._mc_client._post(url=self._build_path(list_id, 'members', subscriber_hash, 'notes'), data=data)
        self.note_id = response['id']
        return response


    def all(self, list_id, subscriber_hash, get_all=False, **queryparams):
        """
        Get recent notes for a specific list member.

        :param list_id: The unique id for the list.
        :type list_id: :py:class:`str`
        :param subscriber_hash: The MD5 hash of the lowercase version of the
          list member’s email address.
        :type subscriber_hash: :py:class:`str`
        :param get_all: Should the query get all results
        :type get_all: :py:class:`bool`
        :param queryparams: The query string parameters
        queryparams['fields'] = []
        queryparams['exclude_fields'] = []
        queryparams['count'] = integer
        queryparams['offset'] = integer
        """
        self.list_id = list_id
        self.subscriber_hash = subscriber_hash
        self.note_id = None
        if get_all:
            return self._iterate(url=self._build_path(list_id, 'members', subscriber_hash, 'notes'), **queryparams)
        else:
            return self._mc_client._get(url=self._build_path(list_id, 'members', subscriber_hash, 'notes'), **queryparams)


    def get(self, list_id, subscriber_hash, note_id, **queryparams):
        """
        Get a specific note for a specific list member.

        :param list_id: The unique id for the list.
        :type list_id: :py:class:`str`
        :param subscriber_hash: The MD5 hash of the lowercase version of the
          list member’s email address.
        :type subscriber_hash: :py:class:`str`
        :param note_id: The id for the note.
        :type note_id: :py:class:`str`
        :param queryparams: The query string parameters
        queryparams['fields'] = []
        queryparams['exclude_fields'] = []
        """
        self.list_id = list_id
        self.subscriber_hash = subscriber_hash
        self.note_id = note_id
        return self._mc_client._get(
            url=self._build_path(list_id, 'members', subscriber_hash, 'notes', note_id),
            **queryparams
        )


    def update(self, list_id, subscriber_hash, note_id, data):
        """
        Update a specific note for a specific list member.

        :param list_id: The unique id for the list.
        :type list_id: :py:class:`str`
        :param subscriber_hash: The MD5 hash of the lowercase version of the
          list member’s email address.
        :type subscriber_hash: :py:class:`str`
        :param note_id: The id for the note.
        :type note_id: :py:class:`str`
        :param data: The request body parameters
        :type data: :py:class:`dict`
        """
        self.list_id = list_id
        self.subscriber_hash = subscriber_hash
        self.note_id = note_id
        return self._mc_client._patch(
            url=self._build_path(list_id, 'members', subscriber_hash, 'notes', note_id),
            data=data
        )


    def delete(self, list_id, subscriber_hash, note_id):
        """
        Delete a specific note for a specific list member.

        :param list_id: The unique id for the list.
        :type list_id: :py:class:`str`
        :param subscriber_hash: The MD5 hash of the lowercase version of the
          list member’s email address.
        :type subscriber_hash: :py:class:`str`
        :param note_id: The id for the note.
        :type note_id: :py:class:`str`
        """
        self.list_id = list_id
        self.subscriber_hash = subscriber_hash
        self.note_id = note_id
        return self._mc_client._delete(url=self._build_path(list_id, 'members', subscriber_hash, 'notes', note_id))
